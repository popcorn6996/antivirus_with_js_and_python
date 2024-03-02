import speedtest

def test_internet_speed():
    st = speedtest.Speedtest()
    
    print('Testing Internet Speed')
    
    downlaod_speed = st.download() / 10 **6
    upload_speed = st.upload() / 10 **6
    ping_speed = st.results.ping
    
    
    print(f'Download speed: {downlaod_speed:.2f} Mbps')
    print(f'Upload speed: {upload_speed:.2f} Mbps')
    print(f'Ping speed: {ping_speed:.2f} Mbps')
    
    
if __name__ == "__main__":
    test_internet_speed()    