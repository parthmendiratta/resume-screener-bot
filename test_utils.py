from utils import read_pdf

resume = read_pdf("sample_data/resume.pdf")
jd = read_pdf("sample_data/job_description.pdf")

print("Resume Preview:\n", resume[:300])
print("\nJob Description Preview:\n", jd[:300])
