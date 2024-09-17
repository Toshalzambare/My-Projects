"""    To Genrate Dummy Database of List of hospitals in city """"





import pandas as pd
from faker import Faker
import random
from datetime import datetime

fake = Faker()

# Expanded list of Delhi locations
locations = [
    'Panchavati', 'Gangapur Road', 'Indira Nagar', 'Nashik Road', 'Cidco', 'Mahatma Nagar', 'Satpur', 'College Road',
    'Dwarka', 'Ashok Stambh', 'Pathardi Phata', 'Sharanpur Road', 'Sinnar', 'Deolali Camp', 'Adgaon', 'Meri Colony',
    'Ambad', 'Trimbak Road', 'Bytco Point', 'Jail Road', 'Bhadrakali', 'Untwadi', 'Chandak Circle', 'Mumbai Naka',
    'Tapovan', 'Sarda Circle', 'Makhmalabad', 'Govind Nagar', 'Upnagar', 'Mhasrul', 'Malegaon Stand', 'Ozar', 
    'Kusmadi', 'Pandav Leni', 'Dwarka Circle', 'Nandur Naka', 'Sawarkar Nagar', 'Saptashrungi'
]

# Lists of categories, specializations, qualifications
specializations = [
    'Cardiology', 'Neurology', 'Pulmonology', 'Surgery', 'General Medicine', 'Orthopedics', 'Endocrinology',
    'Pediatrics', 'Oncology', 'Urology', 'ENT', 'Radiology', 'Hematology', 'Gastroenterology', 'Dermatology'
]
categories = [
    'Hospitals', 'Children Hospitals', 'ENT Hospitals', 'Maternity Hospitals', 'Mental Hospitals',
    'Multispeciality Hospitals', 'Private Hospitals', 'Public Hospitals', 'Veterinary Hospitals', 'Clinic',
    'Ayurvedic Hospitals', 'Cancer Hospitals', 'Dental Hospitals', 'Diabetic Centres', 'ESIS Hospitals',
    'Eye Hospitals', 'HIV Hospitals', 'Kidney Hospitals', 'Cardiac Hospitals', 'Government Veterinary Hospitals',
    'Swine Flu Testing Centres', 'Charitable Hospitals', 'Tuberculosis Hospitals', 'Homeopathic Hospitals',
    'Neurological Hospitals', 'Nursing Homes', 'Orthopaedic Hospitals'
]
qualifications = [
    'MBBS', 'MD', 'MS', 'MCh', 'DM', 'DNB', 'FRCS', 'Fellowship', 'PhD', 'BDS'
]
num_entries = 1000

def generate_doctor_info(num_doctors, open_time, close_time, is_multispeciality=False):
    qualifications_list = random.choices(qualifications, k=num_doctors)
    if is_multispeciality:
        specialties = random.sample(specializations, min(num_doctors, 5))
    else:
        specialties = random.choices(specializations, k=num_doctors)
    
    doctor_info = []
    
    for i in range(num_doctors):
        in_time = fake.time(pattern='%I:%M %p')
        out_time = fake.time(pattern='%I:%M %p')
        
        in_datetime = datetime.strptime(in_time, '%I:%M %p')
        out_datetime = datetime.strptime(out_time, '%I:%M %p')
        
        open_datetime = datetime.strptime(open_time, '%I:%M %p')
        close_datetime = datetime.strptime(close_time, '%I:%M %p')
        
        while in_datetime >= out_datetime or in_datetime < open_datetime or out_datetime > close_datetime:
            in_time = fake.time(pattern='%I:%M %p')
            out_time = fake.time(pattern='%I:%M %p')
            in_datetime = datetime.strptime(in_time, '%I:%M %p')
            out_datetime = datetime.strptime(out_time, '%I:%M %p')
        
        doctor_info.append(f"Dr. {fake.first_name()} {fake.last_name()}, {qualifications_list[i]}, {specialties[i]}, In: {in_time}, Out: {out_time}")
    
    return '; '.join(doctor_info)

def generate_hospital():
    if random.random() < 0.70:
        category = 'Clinic'
        num_doctors = 1
        num_specializations = 1
    else:
        category = random.choice([
            'Hospitals', 'Children Hospitals', 'ENT Hospitals', 'Maternity Hospitals', 'Mental Hospitals',
            'Multispeciality Hospitals', 'Private Hospitals', 'Public Hospitals', 'Veterinary Hospitals',
            'Ayurvedic Hospitals', 'Cancer Hospitals', 'Dental Hospitals', 'Diabetic Centres', 'ESIS Hospitals',
            'Eye Hospitals', 'HIV Hospitals', 'Kidney Hospitals', 'Cardiac Hospitals', 'Government Veterinary Hospitals',
            'Swine Flu Testing Centres', 'Charitable Hospitals', 'Tuberculosis Hospitals', 'Homeopathic Hospitals',
            'Neurological Hospitals', 'Nursing Homes', 'Orthopaedic Hospitals'
        ])
        num_doctors = random.randint(3, 6) if category != 'Multispeciality Hospitals' else random.randint(3, 6)
        num_specializations = random.choices([1, 2, 3], weights=[0.35, 0.65, 0.35])[0]
    
    is_multispeciality = category == 'Multispeciality Hospitals'

    open_time = fake.time(pattern='%I:%M %p')
    close_time = fake.time(pattern='%I:%M %p')
    
    while close_time <= open_time:
        close_time = fake.time(pattern='%I:%M %p')
    
    contact = f'{fake.random_number(digits=10, fix_len=True)}'
    
    return {
        'Hospital Name': fake.company() + " Hospital",
        'Location': random.choice(locations),
        'Rating': round(random.uniform(2.5, 5.0), 1),
        'Number of Doctors': num_doctors,
        'Doctor Info': generate_doctor_info(num_doctors, open_time, close_time, is_multispeciality),
        'Specialization': '; '.join(random.sample(specializations, num_specializations)),
        'Open Time': open_time,
        'Close Time': close_time,
        'Total Beds': random.randint(20, 400) if category != 'Clinic' else random.randint(20, 50),
        'Available Beds': random.randint(10, 200) if category != 'Clinic' else random.randint(5, 20),
        'Contact': contact,
        'Patient Capacity': random.randint(100, 600),
        'Available Doctors': num_doctors,
        'Category': category,
        'Dr. In Time': open_time,
        'Dr. Out Time': close_time
    }

data = [generate_hospital() for _ in range(num_entries)]

df = pd.DataFrame(data)
df.to_csv('hospitals_clinics_delhi_with_details.csv', index=False)

print("Dataset generated and saved to 'hospitals_clinics_delhi_with_details.csv'")
