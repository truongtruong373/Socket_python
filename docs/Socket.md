# 1. Giới thiệu 
Vào năm 1980, ARPA (the US government’s Advanced Research Projects Agency) (cơ quan nghiên cứu dự án tiên tiến của chính phủ Hoa Kỳ) đã cung cấp quỹ cho Đại học California ở Berkeyley để phát triển giao thức TCP/IP theo hệ điều hành UNIX. Trong dự án này, một nhóm nghiên cứu đã phát triển một giao diện chương trình ứng dụng (API) về TCP/IP trong mạng máy tính gọi là socket. Socket là một mạng API TCP/IP, được xác định là một loạt các hàm chức năng hoặc quy trình phần mềm về phát triển ứng dụng trong mạng TCP/IP. Một chương trình SOCKET có thể được thực hiện bởi bất cứ ngôn ngữ nào (hỗ trợ giao tiếp mạng) nhưng mà thích hợp nhất là ngôn ngữ Java bởi vì Java có các cơ chế ngoại lệ để xử lý mạnh mẽ các vấn đề phổ biến xảy ra trong các hoạt động I/O và mạng và các cơ sở phân luồng của nó cung cấp một cách để dễ dàng triển khai các máy chủ mạnh mẽ. 
## 1.1 Giao tiếp Client-Server
Một mạng bao gồm các máy tính trong đó có server và các máy khách (client). Server là một chương trình đang cung cấp dịch vụ trong khi máy khách là một chương trình yêu cầu dịch vụ. Server là những máy tính mạnh hay là chuyên dụng để xử lý còn các máy khách (clients) là những máy tính hay các thiết bị khác mà người dùng có thể chạy ứng dụng. Khi các chương trình này được chạy kết quả là một tiến trình giữa máy khách và server được tạo đồng thời và giao tiếp với nhau dựa vào đọc ghi qua socket giống như hình dưới đây.
![[Pasted image 20241209235423.png]](Pasted%20image%2020241209235423.png)
Những socket này là những programing interface được cung cấp bởi giao thức TCP và UDP về giao tiếp stream và datagram tương ứng ở lớp giao vận.  Khi muốn tạo một ứng dụng mạng, nhiệm vụ chính của nhà phát triển là lập trình cho cả chương trình ở client và server. Ở đây ứng dụng ở client và server là độc lập. Khi phát triển một ứng dụng, nhà phát triển cần phải cẩn thận không sử dụng đến các  port được xác định ở RFCs.
## 1.2 Sockets
Thuật ngữ 'socket' được bắt nguồn từ một thiết bị điện/điện thoại được cắm vào một mạng. 
Socket được định nghĩa theo nhiều cách:
* Theo Wikipedia, một mạng socket là một điểm cuối của một luồng tiến trình giao tiếp qua một mạng máy tính. Một socket bao gồm địa chỉ IP và số Port.
* Socket có thể được định nghĩa là end-point của kết nối giữa hai máy tính được xác định bởi địa chỉ IP và số Port. 
* Socket cũng có thể được định nghĩa là một lớp trừu tượng phần mềm dùng để biểu diễn các "điểm cuối" (terminals) của một kết nối giữa hai máy tính. Nói cách khác, socket là một công cụ giúp hai máy tính giao tiếp với nhau qua mạng, bằng cách tạo ra các điểm cuối để gửi và nhận dữ liệu.
* Nó cũng có thể được định nghĩa là một lớp trừu tượng được cung cấp cho lập trình viên ứng dụng để gửi hoặc nhận dữ liệu đến một tiến trình khác.
* Socket là cánh cửa giữa tầng ứng dụng và tầng giao vận.
* Socket là giao diện giữa ứng dụng và mạng.
## 1.3 Chức năng của socket
Một socket có 4 chức năng cơ bản : 
* Kết nối để điều khiển thiết bị
* Gửi dữ liệu 
* Nhận dữ liệu 
* Đóng kết nối
Một socket không thể kết nối nhiều máy chủ trong từng một khoảng thời gian. Tuy nhiên, một socket có thể cùng gửi và nhận dữ liệu từ một host mà nó đã được kết nối. 
## 1.4 Port
Trong mạng máy tính, port dàng riêng cho một ứng dụng hay là tiến trình cụ thể đóng vai trò là điểm cuối giao tiếp trong hệ điều hành của máy tính. Port được liên kết với địa chỉ IP của host giống như là một loại giao thức để sử dụng trong giao tiếp. Mục đích của port là xác định duy nhất ứng dụng hoặc tiến trình chạy trên một máy tính. Các giao thức chủ yếu sử dụng đến port là các giao thức ở lớp giao vận như là TCP, UDP, ... 

![[Pasted image 20241212134019.png]](Pasted%20image%2020241212134019.png)
Một địa chỉ IP không đủ để xác nhận một server duy nhất, bởi vì có nhiều chương trình chạy trên một thiết bị. Vì vậy ta cần phải dùng đến port. Khi cài đặt client hoặc server, chúng ta cần phải chọn port mà cả client và serve đều kết nối với nhau. Ở đây port không phải là port vật lý, một port logic được xác định bởi 16 bits. Từ 0 đến 1024 là các port dành riêng hỗ trợ cho các dịch vụ của máy tính mà user không được sử dụng đến được quy định trong RFCs.
* ftp 21/tcp
* telnet 23/tcp
* smtp 25/tcp
* http 80/tcp,udp
* https 443/tcp,udp
Ở user-level nói chung được sử dụng các port có giá trị > 1024.
# 2. Network Programming with Socket
## 2.1 Socket Programming 
TCP cung cấp một dịch vụ hướng kết nối, bởi vì nó dựa trên kết nối giữa client và server. Hướng kết nối có nghĩa là một kết nối được thiết lập trước các tiến trình trao đổi dữ liệu. TCP là một dịch vụ tin cậy vì khi một TCP client gửi dữ liệu đến server cần 1 bản tin phúc đáp trở lại. Nếu bản tin phúc đáp không được nhận thì TCP sẽ đợi qua thời gian time out rồi gửi lại dữ liệu. 
Những tiến trình chạy trên những thiết bị khác nhau giao tiếp với nhau bằng cách gửi các tin nhắn vào socket. Mỗi tiến trình giống như một ngôi nhà và socket giống như là cánh cửa. Giống như trong hình dưới đây thì socket giống như là một cánh cửa giữa tiến trình ở lớp ứng dụng với TCP.
![[Pasted image 20241212230558.png]](Pasted%20image%2020241212230558.png)
Dưới góc độ của lớp ứng dụng, kết nối TCP là một đường ống ảo trực tiếp giữa client và server. Tiến trình ở client có thể gửi tùy ý các byte vào socket của client đó, TCP sẽ đảm bảo rằng tiến trình ở server sẽ nhận được mỗi khi một byte được gửi. Hơn thế nữa, giống như là con người có thể vừa đi ra vừa đi vào một cánh cửa thì một tiến trình của client cũng có thể vừa truyền và vừa nhận dữ liệu từ socket của nó. 
## 2.2 Socket sử dụng TCP
![[Pasted image 20241212231834.png]](Pasted%20image%2020241212231834.png)
Ở phần Server Side, thực hiện hàm 'bind' để cố định một cổng nhất định và địa chỉ IP, 'listen' để đợi yêu cầu đến trên port và 'accept' để chấp nhận những kết nối từ những client tương ứng. Client sẽ thực hiện 3-way handshake để tạo một kết nối TCP với server. Lúc này thì client và server có thể giao tiếp với nhau bằng cách ghi và đọc từ socket được tạo ra giữa client và server. Và khi mà giao tiếp hoàn thành, dùng 'close' để đóng kết nối.
## 2.3 Socket sử dụng UDP
UDP là một giao thức datagram, connection-less. Trong trường hợp này client không thiết lập kết nối với server như trong TCP. Thay vào đó, client sẽ gửi một datagram đến server sử dụng hàm 'sendto' với yêu cầu phải có địa chỉ của đích và địa chỉ port. Tương tự, server cũng sẽ không chấp nhận kết nối từ một client. Thay vào đó, server sẽ chỉ gọi đến 'receivefrom' đợi dữ liệu đến từ client. 'receive' sẽ trả về địa chỉ của client và datagram vì vậy mà server cũng có thể gửi phản hồi lại client. 
![[Pasted image 20241212234604.png]](Pasted%20image%2020241212234604.png)
Error
