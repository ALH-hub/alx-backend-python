#!/usr/bin/env python3
"""test for client module"""
from client import GithubOrgClient
from parameterized import parameterized
from unittest.mock import patch, Mock, PropertyMock
from unittest import TestCase, main
import client


class TestGithubOrgClient(TestCase):
    """class to test the GithubOrgClient class"""
    @parameterized.expand([
        ("google"),
        ("abc"),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """test the org method"""
        test_class = GithubOrgClient(org_name)
        test_class.org()
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")

    def test_public_repos_url(self):
        """test the _public_repos_url method"""
        test_class = GithubOrgClient("google")
        with patch.object(GithubOrgClient, 'org',
                          new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {"repos_url": "http://google.com"}
            self.assertEqual(test_class._public_repos_url, "http://google.com")


if __name__ == "__main__":
    main()
