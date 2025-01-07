import threading
import serial
import paramiko
import time
from mobly import base_test
from mobly import test_runner

class HelloWorldTest(base_test.BaseTestClass):

    def setup_class(self):
        # 这里可以执行任何初始化操作，现阶段不需要连接 Android 设备
        print("A2DP sink test setup")

    def test_sink(self):
        # 启动读取串口数据的线程
        serial_thread = threading.Thread(target=self.read_from_serial, daemon=True)
        serial_thread.start()

        # 启动播放音频的线程
        audio_thread = threading.Thread(target=self.play_audio, daemon=True)
        audio_thread.start()

        # 等待音频播放线程结束（因为音频播放是阻塞的，所以可以等待它完成）
        audio_thread.join()

        # 音频播放结束后，返回 "passed"
        print("Audio play completed: passed")

    def read_from_serial(self):
        try:
            # 配置串口COM4，波特率115200
            ser = serial.Serial('COM4', 115200, timeout=1)  # 请根据你的操作系统和设备调整端口名称
            print("串口连接成功！")

            while True:
                if ser.in_waiting > 0:  # 如果串口中有数据可读
                    line = ser.readline().decode('utf-8').strip()  # 读取一行数据并解码
                    print(f"串口数据: {line}")

                time.sleep(0.1)  # 每0.1秒检查一次串口数据

        except serial.SerialException as e:
            print(f"串口连接错误: {e}")
        finally:
            if 'ser' in locals():
                ser.close()
                print("串口连接已关闭")

    def play_audio(self):
        try:
            # 使用paramiko通过SSH命令播放音频
            hostname = '10.4.153.9'  # Linux 服务器的 IP 地址
            port = 22
            username = 'pi'
            password = 'yahboom'

            # 创建 SSH 客户端实例
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            # 连接到远程设备
            ssh.connect(hostname, port=port, username=username, password=password)
            print("SSH连接已建立!")

            # 通过 SSH 执行命令播放音频
            command = 'timeout 10s mpg123 /home/pi/Downloads/bensound-curiouschild.mp3'
            stdin, stdout, stderr = ssh.exec_command(command)

            # 输出音频播放的实时反馈
            for line in stdout.readlines():
                print(f"音频播放信息: {line.strip()}")

            # 等待音频播放结束
            stdout.channel.recv_exit_status()  # 等待命令执行完毕

            print("音频播放完成!")

        except Exception as e:
            print(f"SSH连接或命令执行错误: {e}")
        finally:
            ssh.close()
            print("SSH连接已关闭")

    def teardown_class(self):
        # 清理工作
        print("teardown")

if __name__ == '__main__':
    test_runner.main()
