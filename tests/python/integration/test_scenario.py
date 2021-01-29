from dku_plugin_test_utils import dss_scenario

project_key = "PLUGINTESTSENTIMENTANALYSIS"


def test_binary_classification(user_dss_clients):
    dss_scenario.run(client=user_dss_clients, project_key=project_key, scenario_id="TESTBINARYCLASSIFICATION",
                     user="user1")


def test_5_points_scale_classification(user_dss_clients):
    dss_scenario.run(client=user_dss_clients, project_key=project_key, scenario_id="TEST5POINTSSCALECLASSIFICATION",
                     user="default")


def test_different_settings(user_dss_clients):
    dss_scenario.run(client=user_dss_clients, project_key=project_key, scenario_id="Test_different_options",
                     user="default")


def test_edge_cases(user_dss_clients):
    dss_scenario.run(client=user_dss_clients, project_key=project_key, scenario_id="Test_edge_cases",
                     user="default")


def test_partition_by_language(user_dss_clients):
    dss_scenario.run(client=user_dss_clients, project_key=project_key, scenario_id="Test_partition_by_language",
                     user="default")
