def test_all_values(env, exam, platform, prot, loc, prods):
    assert env in ['dev', 'staging', 'prod']
    assert exam in ['alpha', 'beta', 'unit', 'module', 'integration']
    assert platform in ['Linux', 'Windows', 'MacOS']
    assert prot in ['https', 'sftp', 'ssh']
    assert loc in ['chennai', 'bangalore', 'kolkota']
    assert prods in ['dell', 'lenovo', 'hp']