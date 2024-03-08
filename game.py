import pygame
import sys

# Khởi tạo Pygame
pygame.init()

# Màu sắc
WHITE = (255, 255, 255)

# Kích thước cửa sổ
WIDTH, HEIGHT = 800, 600

# Tạo cửa sổ
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Two Player")

# Load hình ảnh nhân vật
player1_img = pygame.image.load('image_one.png')
player2_img = pygame.image.load('image_two.png')

# Scale hình ảnh cho nhân vật 1 và nhân vật 2
player1_img = pygame.transform.scale(player1_img, (50, 50))
player2_img = pygame.transform.scale(player2_img, (50, 50))

# Vị trí ban đầu của hai nhân vật
# Mỗi mảng gồm 2 phần tử tượng trưng cho tọa độ x, y, về cơ bản di chuyển nhân vật là sẽ thay đổi tọa độ x,y này và cập nhật lại giao diện
player1_pos = [50, 50] # Góc trái trên màn hình với padding 50
player2_pos = [WIDTH - 100, HEIGHT - 100] # Góc phải dưới màn hình với padding 100

# Tốc độ di chuyển
speed = 5

# Vòng lặp chính
running = True
while running:
    # Xử lý sự kiện
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Bắt sự kiện đóng cửa số thì thoát khỏi vòng lặp
            running = False

    # Xử lý đầu vào từ bàn phím
    keys = pygame.key.get_pressed()
    # Nhân vật 1
    if keys[pygame.K_LEFT]: # Mũi tên trái
        player1_pos[0] -= speed
    if keys[pygame.K_RIGHT]: # Mũi tên phải
        player1_pos[0] += speed
    if keys[pygame.K_UP]: # Mũi tên lên
        player1_pos[1] -= speed
    if keys[pygame.K_DOWN]: # Mũi tên xuống
        player1_pos[1] += speed

    # Nhân vật 2
    if keys[pygame.K_a]: # Phím A trái
        player2_pos[0] -= speed
    if keys[pygame.K_d]: # Phím D phải
        player2_pos[0] += speed
    if keys[pygame.K_w]: # Phím W lên
        player2_pos[1] -= speed
    if keys[pygame.K_s]: # Phím S xuống
        player2_pos[1] += speed

    # Vẽ màn hình
    screen.fill(WHITE)
    screen.blit(player1_img, player1_pos) # Hàm blit() được sử dụng để vẽ hình ảnh lên màn hình tại vị trí đã chỉ định.
    screen.blit(player2_img, player2_pos)
    pygame.display.flip() # hàm pygame.display.flip() được gọi để cập nhật màn hình, hiển thị các thay đổi vừa được thực hiện.

    # Giới hạn vị trí của nhân vật trong cửa sổ
    player1_pos[0] = max(0, min(WIDTH - 50, player1_pos[0]))
    player1_pos[1] = max(0, min(HEIGHT - 50, player1_pos[1]))
    player2_pos[0] = max(0, min(WIDTH - 50, player2_pos[0]))
    player2_pos[1] = max(0, min(HEIGHT - 50, player2_pos[1]))

    # Điều chỉnh tốc độ vòng lặp
    pygame.time.Clock().tick(60)

# Kết thúc Pygame
pygame.quit()
sys.exit()