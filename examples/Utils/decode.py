from sdk_cloud_dfe import Util  # Supondo que Util seja o nome do arquivo e da classe

try:
    # exemplo base64 + compactado/zipado
    data = 'H4sIAAAAAAAACgtJrSjJV0jOzy1ITC5JTMnXr8osAFIATnk5SBcAAAA='
    
    # exemplo de base64
    # data = 'dGV4dG8gYSBzZXIgZGVjb2RpZmljYWRv'

    resp = Util.decode(data)

    print(resp)
except Exception as e:
    print(e)