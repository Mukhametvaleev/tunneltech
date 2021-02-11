python3 -m venv venv && source venv/bin/activate && pip install --upgrade pip
pip install -e '.[development]'
npm install --prefix ./frontend frontend
python3 -m grpc_tools.protoc -I ./proto/windtunnel --python_out=./proto --grpc_python_out=./proto ./proto/windtunnel/*.proto
sed -i -- 's/import windtunneltypes_pb2/import proto.windtunneltypes_pb2/g' proto/*.py
rm proto/*.py--
