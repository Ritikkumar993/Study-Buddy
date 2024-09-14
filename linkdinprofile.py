import requests
from bs4 import BeautifulSoup
def get_leetcode_data(username):

    url = "https://leetcode.com/graphql"
    query = """
    query getLeetCodeData($username: String!) {
      userProfile: matchedUser(username: $username) {
        username
        profile {
          userAvatar
          reputation
          ranking
        }
        submitStats {
          acSubmissionNum {
            difficulty
            count
          }
          totalSubmissionNum {
            difficulty
            count
          }
        }
      }
      userContestRanking(username: $username) {
        attendedContestsCount
        rating
        globalRanking
        totalParticipants
        topPercentage
      }
      recentSubmissionList(username: $username) {
        title
        statusDisplay
        lang
      }
    }
    """
    variables = {
        "username": username
    }
    response = requests.post(url, json={'query': query, 'variables': variables})
    data = response.json()

    if 'errors' in data:
        print("Error:", data['errors'])
        return None

    return data['data']

    
print(get_leetcode_data(sreecharan9484))