from urllib.parse import quote


def test_unregister_success_removes_participant(client):
    activity_name = "Basketball Team"
    email = "liam@mergington.edu"

    response = client.delete(
        f"/activities/{quote(activity_name)}/participants", params={"email": email}
    )

    assert response.status_code == 200
    assert response.json()["message"] == f"Unregistered {email} from {activity_name}"

    activities = client.get("/activities").json()
    assert email not in activities[activity_name]["participants"]


def test_unregister_unknown_activity_returns_404(client):
    response = client.delete(
        "/activities/Unknown%20Club/participants", params={"email": "test@mergington.edu"}
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_unregister_missing_participant_returns_404(client):
    activity_name = "Basketball Team"

    response = client.delete(
        f"/activities/{quote(activity_name)}/participants",
        params={"email": "absent@mergington.edu"},
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Participant not found for this activity"
