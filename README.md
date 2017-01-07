# qingstor-demo-auth-server

## Installation

```bash
git clone https://github.com/yunify/qingstor-demo-auth-server.git
cd qingstor-demo-auth-server
pip install -r requirements
```

## Usage

### Setup environment variable

```bash
export ACCESS_KEY_ID="ACCESS_KEY_ID_EXAMPLE"
export SECRET_ACCESS_KEY="SECRET_ACCESS_KEY_EXAMPLE"
export ZONE="pek3a"
```

> `zone` should be set either by environment variable or set in every request

### Run demo

```bash
python demo.py
```

### Post data

#### GET Service

```bash
curl -H "Content-Type: application/json" -d '{"method":"GET", "url":"/", "headers":{"Date":"Wed, 10 Dec 2014 17:20:31 GMT"}}' 127.0.0.1:5000
```

If success, server will return an authorized string like:

```text
QS ACCESS_KEY_ID_EXAMPLE:vIWg/qAxvXlcFRb9uzYmdIM9tiF6EuM6SC3i13yLzH8=
```

#### PUT Object

```bash
curl -H "Content-Type: application/json" -d '{"method":"PUT", "url":"/test-bucket/test.json","zone":"pek3a","headers":{"Content-Type":"application/json","Date":"Wed, 10 Dec 2014 17:20:31 GMT"}}' 127.0.0.1:5000
```

If success, server will return an authorized string like:

```text
QS ACCESS_KEY_ID_EXAMPLE:bpfE8ix/fllVYOaSLAGZ/+SO23M0ESaTAqZKapxbwV4=
```

#### GET Bucket ACL

```bash
curl -H "Content-Type: application/json" -d '{"method":"GET", "url":"/test-bucket?acl","zone":"pek3a","headers":{"Date":"Wed, 10 Dec 2014 17:20:31 GMT"}}' 127.0.0.1:5000
```

If success, server will return an authorized string like:

```text
QS ACCESS_KEY_ID_EXAMPLE:aMm0TPNafQW391RE1aZLrhfTLPZpVzw+0qiGafhAgOw=
```
