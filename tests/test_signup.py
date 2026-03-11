from urllib.parse import quote


def test_signup_success_adds_participant(client):
    activity_name = "Basketball Team"
    email = "newstudent@mergington.edu"

    response = client.post(f"/activities/{quote(activity_name)}/signup", params={"email": email})

    assert response.status_code == 200
    assert response.json()["message"] == f"Signed up {email} for {activity_name}"

    activities = client.get("/activities").json()
    assert email in activities[activity_name]["participants"]


def test_signup_duplicate_returns_400(client):
    activity_name = "Basketball Team"
    email = "duplicate@mergington.edu"

    first = client.post(f"/activities/{quote(activity_name)}/signup", params={"email": email})
    second = client.post(f"/activities/{quote(activity_name)}/signup", params={"email": email})

    assert first.status_code == 200
    assert second.status_code == 400
    assert second.json()["detail"] == "Student already signed up for this activity"


def test_signup_unknown_activity_returns_404(client):
    response = client.post("/activities/Unknown%20Club/signup", params={"email": "test@mergington.edu"})

    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"
