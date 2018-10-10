login_query = """{
  viewer{
    login
  }
}"""

all_query = """
{
  repository(owner: "%s", name: "%s") {
    name
    pullRequests(first:100){
      pageInfo{
        endCursor
        hasNextPage
      }
      nodes{
        publishedAt
        id
      }
    }
    ref(qualifiedName: "master"){
      target{
        ... on Commit{
          history(first:100,since:"%sT00:00:00",until:"%sT23:59:59"){
            pageInfo {
              endCursor
              hasNextPage
            }
            totalCount
            edges {
              node {
                author{
                  email
                }
                pushedDate
              }
            }
          }
        }
      }
    }
  }
}
"""
all_query_with_pager = """
{
  repository(owner: "%s", name: "%s") {
    name
    pullRequests(first:100,after:"%s"){
      pageInfo{
        endCursor
        hasNextPage
      }
      nodes{
        publishedAt
        id
      }
    }
    ref(qualifiedName: "master"){
      target{
        ... on Commit{
          history(first:100,after:"%s",since:"%sT00:00:00",until:"%sT23:59:59"){
            pageInfo {
              endCursor
              hasNextPage
            }
            totalCount
            edges {
              node {
                author{
                  email
                }
                pushedDate
              }
            }
          }
        }
      }
    }
  }
}
"""

pr_query_with_pager = """
{
  repository(owner: "%s", name: "%s") {
    name
    pullRequests(first:100,after:"%s"){
      pageInfo{
        endCursor
        hasNextPage
      }
      nodes{
        publishedAt
        id
      }
    }
  }
}
"""

commit_query_with_pager = """
{
  repository(owner: "%s", name: "%s") {
    name
    ref(qualifiedName: "master"){
      target{
        ... on Commit{
          history(first:100,after:"%s",since:"%sT00:00:00",until:"%sT23:59:59"){
            pageInfo {
              endCursor
              hasNextPage
            }
            totalCount
            edges {
              node {
                author{
                  email
                }
                pushedDate
              }
            }
          }
        }
      }
    }
  }
}
"""

organ_all_query = """
{
  organization(login:"%s"){
    repositories(first:100,orderBy:{field:STARGAZERS,direction:DESC},isFork:false){
      pageInfo{
        hasNextPage
        endCursor
      }
      nodes{
        name,
        stargazers{
          totalCount
        },
      }
    }
  }
}
"""

organ_all_query_with_pager = """
{
  organization(login:"%s"){
    repositories(first:100,after:"%s",orderBy:{field:STARGAZERS,direction:DESC},isFork:false){
      pageInfo{
        hasNextPage
        endCursor
      }
      nodes{
        name,
        stargazers{
          totalCount
        },
      }
    }
  }
}
"""

user_all_query = """
{
  user(login:"%s"){
    repositories(first:100,orderBy:{field:STARGAZERS,direction:DESC},isFork:false){
      pageInfo{
        hasNextPage
        endCursor
      }
      nodes{
        name,
        owner {
          login
        }
        stargazers{
          totalCount
        },
      }
    }
  }
}
"""

user_all_query_with_pager = """
{
  user(login:"%s"){
    repositories(first:100,after:"%s",orderBy:{field:STARGAZERS,direction:DESC},isFork:false){
      pageInfo{
        hasNextPage
        endCursor
      }
      nodes{
        name,
        owner {
          login
        }
        stargazers{
          totalCount
        },
      }
    }
  }
}
"""
