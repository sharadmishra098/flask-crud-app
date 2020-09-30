from flask import abort, flash, redirect, render_template, url_for, Blueprint
from flask_login import current_user, login_required

from .forms import DepartmentForm, RoleForm, EmployeeAssignForm
from .. import db
from ..models import Department, Role, Employee

admin = Blueprint('admin', __name__)


def check_admin():
    """
    Prevent non-admins to login
    """
    if not current_user.is_admin:
        abort(403)


@admin.route('/departments', methods=['GET'])
@login_required
def list_departments():
    """list the departments added"""
    check_admin()
    departments = Department.query.all()
    return render_template('admin/departments/departments.html',
                           departments=departments, title="Departments")


@admin.route('/departments/add', methods=['GET', 'POST'])
@login_required
def add_department():
    """add more departmnets"""
    check_admin()
    add_department = True
    form = DepartmentForm()
    if form.validate_on_submit():
        department = Department(name=form.name.data,
                                description=form.description.data)
        try:
            db.session.add(department)
            db.session.commit()
            flash('You have successfully added a new department.')
        except Exception:
            flash('Error: department name already exists.', 'error')
        return redirect(url_for('admin.list_departments'))

    return render_template('admin/departments/department.html', action="Add",
                           add_department=add_department, form=form,
                           title="Add Department")


@admin.route('/departments/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_department(id):
    """edit departments"""
    check_admin()

    add_department = False

    department = Department.query.get_or_404(id)
    form = DepartmentForm()
    if form.validate_on_submit():
        department.name = form.name.data
        department.description = form.description.data
        try:
            db.session.add(department)
            db.session.commit()
            flash('You have successfully edited the department.')
        except Exception:
            flash('Error: This Department already exists.', 'error')
        return redirect(url_for('admin.list_departments'))

    form.description.data = department.description
    form.name.data = department.name
    return render_template('admin/departments/department.html', action="Edit",
                           add_department=add_department, form=form,
                           department=department, title="Edit Department")


@admin.route('/departments/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_department(id):
    """to delete the existing department"""
    check_admin()

    department = Department.query.get_or_404(id)
    db.session.delete(department)
    db.session.commit()
    flash('You have successfully deleted the department.')

    return redirect(url_for('admin.list_departments'))


@admin.route('/roles')
@login_required
def list_roles():
    """list all the roles"""
    check_admin()
    roles = Role.query.all()
    return render_template('admin/roles/roles.html',
                           roles=roles, title='Roles')


@admin.route('/roles/add', methods=['GET', 'POST'])
@login_required
def add_role():
    """add more roles"""
    check_admin()

    add_role = True

    form = RoleForm()
    if form.validate_on_submit():
        role = Role(name=form.name.data,
                    description=form.description.data)

        try:
            db.session.add(role)
            db.session.commit()
            flash('You have successfully added a new role.')
        except Exception:
            flash('Error: role name already exists.', 'error')

        return redirect(url_for('admin.list_roles'))

    return render_template('admin/roles/role.html', add_role=add_role,
                           form=form, title='Add Role')


@admin.route('/roles/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_role(id):
    """edit roles"""
    check_admin()

    add_role = False

    role = Role.query.get_or_404(id)
    form = RoleForm()
    if form.validate_on_submit():
        role.name = form.name.data
        role.description = form.description.data
        try:
            db.session.add(role)
            db.session.commit()
            flash('You have successfully edited the role.')
        except Exception:
            flash('Error: This role already exists.', 'error')

        return redirect(url_for('admin.list_roles'))

    form.description.data = role.description
    form.name.data = role.name
    return render_template('admin/roles/role.html', add_role=add_role,
                           form=form, title="Edit Role")


@admin.route('/roles/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_role(id):
    """delete roles"""
    check_admin()

    role = Role.query.get_or_404(id)
    db.session.delete(role)
    db.session.commit()
    flash('You have successfully deleted the role.')

    return redirect(url_for('admin.list_roles'))


@admin.route('/employees')
@login_required
def list_employees():
    """list the employees"""
    check_admin()

    employees = Employee.query.all()
    return render_template('admin/employees/employees.html',
                           employees=employees, title='Employees')


@admin.route('/employees/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_employee(id):
    """delete the employees"""
    check_admin()

    employee = Employee.query.get_or_404(id)
    db.session.delete(employee)
    db.session.commit()

    flash('You have successfully deleted the employee.')

    return redirect(url_for('admin.list_employees'))


@admin.route('/employees/assign/<int:id>', methods=['GET', 'POST'])
@login_required
def assign_employee(id):
    """assign department and roles"""
    check_admin()

    employee = Employee.query.get_or_404(id)

    if employee.is_admin:
        abort(403)

    form = EmployeeAssignForm()
    if form.validate_on_submit():
        employee.department_taken = form.department.data
        employee.rolled_in = form.role.data
        db.session.add(employee)
        db.session.commit()
        flash('You have successfully assigned a department and role.')

        # redirect to the roles page
        return redirect(url_for('admin.list_employees'))
    form.department.data = employee.department_taken
    form.role.data = employee.rolled_in
    return render_template('admin/employees/employee.html',
                           employee=employee, form=form,
                           title='Assign Employee')
