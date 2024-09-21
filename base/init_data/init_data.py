import os
import random
from datetime import datetime, timedelta
import django
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

# Import các model
from user.models.user import User, Role
from user.models.role import Role
from user_profile.models.customer_profile import CustomerProfile
from user_profile.models.coach_profile import CoachProfile
from workout.models.exercise import Exercise
from workout.models.workout_goal import WorkoutGoal
from workout.models.workout_plan import WorkoutPlan
from workout.models.workout_schedule import WorkoutSchedule

# Khởi tạo Faker
fake = Faker()

# Tạo dữ liệu giả cho Role
def create_roles():
    roles = [
        {'role_name': 'admin', 'permission': {}},
        {'role_name': 'sale', 'permission': {}},
        {'role_name': 'customer', 'permission': {}},
        {'role_name': 'coach', 'permission': {}},
    ]
    for role_data in roles:
        role, created = Role.objects.get_or_create(**role_data)
        if created:
            print(f"Created role: {role.role_name}")

# Tạo dữ liệu giả cho User
def create_users(num_users=20):
    roles = Role.objects.all()
    for _ in range(num_users):
        role = random.choice(roles)
        user = User.objects.create(
            email=fake.email(),
            password='password123',  # Mã hóa mật khẩu nếu cần thiết
            role=role,
            status=random.choice([1, 2, 3]),
            email_verified=fake.boolean(),
            avatar_url=fake.image_url()
        )
        print(f"Created user: {user.email}")

# Tạo dữ liệu giả cho CoachProfile
def create_coach_profiles():
    coach_users = User.objects.filter(role__role_name='coach')
    for user in coach_users:
        profile = CoachProfile.objects.create(
            coach=user,
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            phone=fake.phone_number(),
            address=fake.address(),
            gender=random.choice([0, 1]),  # 0: Female, 1: Male
            birthday=fake.date_of_birth(minimum_age=25, maximum_age=50),
            height=round(random.uniform(150.0, 200.0), 2),
            weight=round(random.uniform(50.0, 100.0), 2),
            start_date=fake.date_this_decade(),
            extra_data={"experience": fake.text()}
        )
        print(f"Created coach profile for: {user.email}")

# Tạo dữ liệu giả cho CustomerProfile
def create_customer_profiles():
    customer_users = User.objects.filter(role__role_name='customer')
    for user in customer_users:
        profile = CustomerProfile.objects.create(
            customer=user,
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            phone=fake.phone_number(),
            address=fake.address(),
            gender=random.choice([0, 1]),  # 0: Female, 1: Male
            birthday=fake.date_of_birth(minimum_age=18, maximum_age=60)
        )
        print(f"Created customer profile for: {user.email}")

# Tạo dữ liệu giả cho Exercise
def create_exercises(num_exercises=10):
    for _ in range(num_exercises):
        exercise = Exercise.objects.create(
            name=fake.word(),
            duration=random.randint(10, 120),  # Thời gian tập (phút)
            repetitions=f"{random.randint(5, 20)} reps",
            image_url=fake.image_url()
        )
        print(f"Created exercise: {exercise.name}")

# Tạo dữ liệu giả cho WorkoutGoal
def create_workout_goals():
    customers = User.objects.filter(role__role_name='customer')
    coaches = User.objects.filter(role__role_name='coach')
    for customer in customers:
        coach = random.choice(coaches)
        goal = WorkoutGoal.objects.create(
            customer=customer,
            coach=coach,
            weight=round(random.uniform(50.0, 100.0), 2),
            extra_data={"goal": fake.text()}
        )
        print(f"Created workout goal for customer: {customer.email}")

# Tạo dữ liệu giả cho WorkoutPlan
def create_workout_plans():
    customers = User.objects.filter(role__role_name='customer')
    coaches = User.objects.filter(role__role_name='coach')
    for customer in customers:
        coach = random.choice(coaches)
        plan = WorkoutPlan.objects.create(
            customer=customer,
            coach=coach,
            start_date=fake.date_this_year(),
            expire_date=fake.date_this_year(),
            details={"plan": fake.text()}
        )
        print(f"Created workout plan for customer: {customer.email}")

# Tạo dữ liệu giả cho WorkoutSchedule
def create_workout_schedules():
    customers = User.objects.filter(role__role_name='customer')
    coaches = User.objects.filter(role__role_name='coach')
    exercises = Exercise.objects.all()
    for customer in customers:
        coach = random.choice(coaches)
        exercise = random.choice(exercises)
        schedule = WorkoutSchedule.objects.create(
            customer=customer,
            coach=coach,
            exercise=exercise,
            date=fake.date_this_year(),
            start_time=fake.time(),
            end_time=fake.time(),
            duration=random.randint(30, 120),
            overview=fake.text()
        )
        print(f"Created workout schedule for customer: {customer.email}")

# Chạy các hàm tạo dữ liệu giả
if __name__ == '__main__':
    create_roles()
    create_users(num_users=50)  # Số lượng người dùng
    create_coach_profiles()
    create_customer_profiles()
    create_exercises(num_exercises=20)
    create_workout_goals()
    create_workout_plans()
    create_workout_schedules()
