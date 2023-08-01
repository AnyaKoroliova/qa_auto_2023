import pytest


@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user('defunkt')
    assert user['login'] == 'defunkt'


@pytest.mark.api
def test_user_not_exists(github_api):
    r = github_api.get_user('butenkosergii')
    assert r['message'] == 'Not Found'


@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo('become-qa-auto')
    assert r['total_count'] == 42
    assert 'become-qa-auto' in r['items'][0]['name']


@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo('sergiibutenko_repo_non_exist')
    assert r['total_count'] == 0


@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo('s')
    assert r['total_count'] != 0



# Individual Tests for GitHub API
@pytest.mark.api_my
def test_create_issue(github_api):
    r1 = github_api.create_issue('AnyaKoroliova', 'qa_auto_2023', data={"title":"Found a bug","body":"I'm having a problem with this.","labels":["bug"]})
    r2 = github_api.create_issue('AnyaKoroliova', 'qa_auto_2023', data={"title":"New bug","body":"Bug or feature.","labels":["feature"]})
    assert 'message' not in r1
    assert 'message' not in r2


@pytest.mark.api_my
def test_list_of_issues(github_api):
    r = github_api.list_of_issues('AnyaKoroliova', 'qa_auto_2023', 'bug')
    assert len(r) > 0
    assert 'bug' in r[0]['labels'][0]['name']


@pytest.mark.api_my
def test_update_issue(github_api):
    r = github_api.list_of_issues('AnyaKoroliova', 'qa_auto_2023', 'bug')
    issue_id = r[0]['number']
    ur = github_api.update_issues('AnyaKoroliova', 'qa_auto_2023', issue_id, data={"title":"Edited issue 3"})
    i = github_api.get_issues('AnyaKoroliova', 'qa_auto_2023', issue_id)
    assert i['title'] == "Edited issue 3"


@pytest.mark.api_my
def test_create_comment(github_api):
    a = github_api.list_of_commit('AnyaKoroliova', 'qa_auto_2023')
    assert 'message' not in a
    commit_sha = a[0]['sha']
    b = github_api.create_comment('AnyaKoroliova', 'qa_auto_2023', commit_sha, data={"body": "test comment 2"})
    assert 'message' not in b
    assert b['body'] == "test comment 2"


@pytest.mark.api_my
def test_delete_comment(github_api):
    r = github_api.delete_comment('AnyaKoroliova', 'qa_auto_2023', 999)
    body = r.json()
    assert r.status_code == 404
    assert 'message' in body
    assert body['message'] == 'Not Found'