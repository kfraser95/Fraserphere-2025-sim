from src.link_budget import P_r_dBm  # (modify to return value)

def test_1AU_link():
    assert abs(float(P_r_dBm) + 136.2) < 0.1