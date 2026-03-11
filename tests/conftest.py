from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

import src.app as app_module


@pytest.fixture
def client():
    return TestClient(app_module.app)


@pytest.fixture(autouse=True)
def reset_activities_state():
    baseline = deepcopy(
        {
            "Basketball Team": {
                "description": "Team practices, drills, and interschool basketball matches",
                "schedule": "Mondays and Wednesdays, 4:00 PM - 5:30 PM",
                "max_participants": 15,
                "participants": ["liam@mergington.edu", "noah@mergington.edu"],
            },
            "Soccer Club": {
                "description": "Soccer training sessions focused on teamwork and fitness",
                "schedule": "Tuesdays and Thursdays, 4:00 PM - 5:30 PM",
                "max_participants": 18,
                "participants": ["ava@mergington.edu", "isabella@mergington.edu"],
            },
            "School Choir": {
                "description": "Vocal training and group performances at school events",
                "schedule": "Wednesdays, 3:30 PM - 5:00 PM",
                "max_participants": 25,
                "participants": ["mia@mergington.edu", "charlotte@mergington.edu"],
            },
            "Drama Club": {
                "description": "Acting workshops and theater productions",
                "schedule": "Fridays, 4:00 PM - 6:00 PM",
                "max_participants": 20,
                "participants": ["amelia@mergington.edu", "harper@mergington.edu"],
            },
            "Debate Team": {
                "description": "Develop public speaking and critical thinking through debates",
                "schedule": "Mondays, 3:30 PM - 5:00 PM",
                "max_participants": 16,
                "participants": ["elijah@mergington.edu", "james@mergington.edu"],
            },
            "Science Club": {
                "description": "Hands-on experiments and science fair project preparation",
                "schedule": "Thursdays, 3:30 PM - 5:00 PM",
                "max_participants": 18,
                "participants": ["benjamin@mergington.edu", "lucas@mergington.edu"],
            },
            "Chess Club": {
                "description": "Learn strategies and compete in chess tournaments",
                "schedule": "Fridays, 3:30 PM - 5:00 PM",
                "max_participants": 12,
                "participants": ["michael@mergington.edu", "daniel@mergington.edu"],
            },
            "Programming Class": {
                "description": "Learn programming fundamentals and build software projects",
                "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
                "max_participants": 20,
                "participants": ["emma@mergington.edu", "sophia@mergington.edu"],
            },
            "Gym Class": {
                "description": "Physical education and sports activities",
                "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
                "max_participants": 30,
                "participants": ["john@mergington.edu", "olivia@mergington.edu"],
            },
        }
    )

    app_module.activities.clear()
    app_module.activities.update(deepcopy(baseline))
    yield
    app_module.activities.clear()
    app_module.activities.update(deepcopy(baseline))
