from pythonping import ping

ping("127.0.0.1", verbose=True, out_format="legacy")

ping(
    "127.0.0.1",
    verbose=True,
    out_format="CISCO",
    count=10,
    payload=bytes(100),
    timeout=2,
)
