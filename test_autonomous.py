from autonomous_engine import (
    autonomous_research_cycle
)

reports = autonomous_research_cycle()

print("\nAUTONOMOUS RESEARCH REPORTS:\n")

for report in reports:

    print("=" * 60)

    print("CURIOSITY:")

    print(report["curiosity"])

    print("\nREASONING:")

    print(report["reasoning"])
    