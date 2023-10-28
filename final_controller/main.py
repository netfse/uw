import pygame
import time
import serial

ser = serial.Serial('/dev/ttyACM0', 9600)

controller_key_actions = {
    pygame.K_w: 'W',  # move forward
    pygame.K_a: 'A',  # turn left
    pygame.K_s: 'S',  # move back
    pygame.K_d: 'D',  # turn right
    pygame.K_UP: 'q',  # rising
    pygame.K_DOWN: 'e',  # dropping
    pygame.K_ESCAPE: 'EXIT',  # stop controller
    pygame.K_k: '`',  # stop moving
    pygame.K_l: '~',  # stop rising
}

pygame.init()

window_width = 300
window_height = 300
window = pygame.display.set_mode((window_width, window_height))

try:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                for key, command in controller_key_actions.items():
                    if keys[key]:
                        if command == 'EXIT':
                            pygame.quit()
                            quit()
                        else:
                            print("Sending command:", command)
                            ser.write(command.encode())
                            break

        window.fill((0, 0, 0))

        keys = pygame.key.get_pressed()
        font = pygame.font.SysFont(None, 90)
        for key, command in controller_key_actions.items():
            if keys[key]:
                if command == 'EXIT':
                    break
                #print("Sending command:", command)
                key_text = pygame.key.name(key)
                key_text_surface = font.render(key_text, True, (255, 255, 255))
                key_text_rect = key_text_surface.get_rect(center=(window_width // 2, window_height // 2))
                window.blit(key_text_surface, key_text_rect)

        pygame.display.update()
        time.sleep(0.1)

except KeyboardInterrupt:
    pass

pygame.quit()