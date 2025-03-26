import scrapy
import re
import pandas as pd
from pathlib import Path

class DataSpider(scrapy.Spider):
    name = "data"
    allowed_domains = ["talentedge.com"]
    start_urls = ["https://talentedge.com/browse-courses"]

    def start_requests(self):
        urls = [
            "https://talentedge.com/iim-kozhikode/professional-certificate-programme-in-hr-management-and-analytics",
            "https://talentedge.com/iim-raipur/certificate-course-machine-learning-for-managers",
            "https://talentedge.com/golden-gate-university/doctor-of-business-administration",
            "https://talentedge.com/iim-lucknow/supply-chain-management",
            "https://talentedge.com/iim-lucknow/advanced-program-in-strategic-management-for-business-excellence",
            "https://talentedge.com/goa-institute-of-management/exectuive-pg-program-in-health-care-management",
            "https://talentedge.com/iim-raipur/executive-certificate-program-in-general-management",
            "https://talentedge.com/iim-raipur/post-graduate-executive-certification-in-human-resource-management-iimr-hr",
            "https://talentedge.com/iim-raipur/executive-certificate-program-in-digital-marketing-course",
            "https://talentedge.com/esgci-school-of-management-paris/doctorate-of-business-administration-esgci",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # Extracting data from the page
        title = " ".join(response.css(".p-collage-name h1.pl-title *::text").getall()).strip()
        description = " ".join(response.css("div.desc_less *::text").getall()).strip()
        # Extract all list items from the course specification div
        course_spec = [item.strip() for item in response.css("div.course-specification li::text").getall()]

# Slice the list to get specific information
        duration = course_spec[2] if len(course_spec) > 2 else None  # 3rd item for Duration
        timing = course_spec[1] if len(course_spec) > 1 else None    # 2nd item for Timing
        start_date = course_spec[3] if len(course_spec) > 3 else None  # 4th item for Course Start Date

        skills = [skill.strip() for skill in response.css("div.key-skills-sec ul li::text").getall()]
        #learning_outcomes = [item.strip() for item in response.css("div.pl-deeper-undstnd ul li::text").getall()]
        eligibility_criteria = [item.strip() for item in response.css("div.eligible-right-top-list ul li::text").getall()]
        #topics = [topic.strip() for topic in response.css("div#syl-tab1 ul > li > strong::text").getall()]
        topics = [topic.strip() for topic in response.css("div.sylab-tab-ul ul.nav.nav-tabs.syl-ul li a::text").getall()]
        faculty_names = [name.strip() for name in response.css("div.facutly-card h4.best-fname::text").getall()]
        institute_name = response.css("div.plc-institute h4.about-ititle::text").get().strip()

        # Extracting fee amounts
        raw_text = response.css("div.program-details-total-pay-amt-right::text").getall()
        full_text = ''.join(raw_text).strip()
        usd_match = re.search(r'USD\s*([\d,]+)', full_text)
        inr_match = re.search(r'INR\s*([\d,]+)\s*(?:\+ GST)?', full_text)
        usd_amount = f"USD {usd_match.group(1)}" if usd_match else None
        inr_amount = f"INR {inr_match.group(1)} {'+ GST' if inr_match.group(0).endswith('+ GST') else ''}" if inr_match else None

        # Extracting faculty descriptions from the data-description attribute
        faculty_descriptions = response.css("div.best-fknomore a.showFacultyDescription::attr(data-description)").getall()
        faculty_descriptions = [desc.strip() for desc in faculty_descriptions]
        faculty_designations = response.css("div.best-fdetail p.best-fdesingnation::text").getall()
        faculty_designations = [designation.strip() for designation in faculty_designations]
        # Handle multiple faculty members (assuming a max of 2 for simplicity)
        faculty_1_name = faculty_names[0] if len(faculty_names) > 0 else ''
        faculty_2_name = faculty_names[1] if len(faculty_names) > 1 else ''
        faculty_1_desc = faculty_descriptions[0] if len(faculty_descriptions) > 0 else ''
        faculty_2_desc = faculty_descriptions[1] if len(faculty_descriptions) > 1 else ''
        # Extract the designation from the <p> tag with class 'best-fdesingnation'
        faculty_1_designation = faculty_designations[0] if len(faculty_designations) > 0 else ''
        faculty_2_designation = faculty_designations[1] if len(faculty_designations) > 1 else ''


        # Print the extracted information
        print(f"Course Link: {response.url}")
        print(f"Title: {title}")
        print(f"Description: {description}")
        print("Duration:", duration)
        print("Timing:", timing)
        print("Course Start Date:", start_date)
        print(f"What you will learn: {'; '.join(skills)}")
        key_skills=[item.strip() for item in response.css("div.key-skills-sec ul li::text").getall()]
        print(f"Skills: {'; '.join(key_skills)}")
        # Extract the content within the <h4> tag with class 'cs-titlec'
        target_students = response.css("div.cs-content h4.cs-titlec::text").get().strip()

        print("Target Students:", target_students)

        print(f"Eligibility criteria: {'; '.join(eligibility_criteria)}")
        print(f"Content: {'; '.join(topics)}")
        print(f"Faculty 1 Name: {faculty_1_name}")
        print(f"Faculty 1 Designation: {faculty_1_designation}")
        print(f"Faculty 1 Description: {faculty_1_desc}")
        print(f"Faculty 2 Name: {faculty_2_name}")
        print(f"Faculty 2 Designation: {faculty_2_designation}")
        print(f"Faculty 2 Description: {faculty_2_desc}")
        print(f"Institution Name: {institute_name}")
        print(f"Fee in INR: {inr_amount}")
        print(f"Fee in USD: {usd_amount}")

        # Data to be saved
        data = {
            "Course Link": [response.url],
            "Title": [title],
            "Description": [description],
            "Duration": [duration],  # Replace with actual duration
            "Timing": [timing],  # Replace with actual timing
            "Course Start Date": [start_date],  # Replace with actual start date
            "What you will learn": ["; ".join(skills)],
            "Skills": ["; ".join(key_skills)],
            "Target students": target_students,  # Replace with actual target students
            "Prerequisites / Eligibility criteria": ["; ".join(eligibility_criteria)],
            "Content": ["; ".join(topics)],
            "Faculty 1 Name": [faculty_1_name],
            "Faculty 1 Designation": [faculty_1_designation],  # Replace with actual designation
            "Faculty 1 Description": [faculty_1_desc],
            "Faculty 2 Name": [faculty_2_name],
            "Faculty 2 Designation": [faculty_2_designation],  # Replace with actual designation
            "Faculty 2 Description": [faculty_2_desc],
            "Institute Name": [institute_name],
            "Fee in INR": [inr_amount],
            "Fee in USD": [usd_amount]
        }

        # Saving the data to Excel
        df = pd.DataFrame(data)
        excel_path = Path("course_data.xlsx")
        if excel_path.exists():
            with pd.ExcelWriter(excel_path, engine="openpyxl", mode="a", if_sheet_exists="overlay") as writer:
                df.to_excel(writer, index=False, header=False, startrow=writer.sheets["Sheet1"].max_row)
        else:
            df.to_excel("course_data.xlsx", index=False)













        
        
        
