-- Заполнение таблицы addresses_address
INSERT INTO addresses_address (country, city, street, house, apartment)
VALUES 
    ('Россия', 'Москва', 'Тверская улица', '12', '34'),
    ('Россия', 'Санкт-Петербург', 'Невский проспект', '45', '12'),
    ('Россия', 'Казань', 'Улица Баумана', '7', '18');

-- Заполнение таблицы stations_station
INSERT INTO stations_station (name, tax_id, address_id)
VALUES 
    ('Москва-Пассажирская', '123456789012', 1),
    ('Санкт-Петербург-Главный', '123456789013', 2),
    ('Казань-Пассажирская', '123456789014', 3);

-- Заполнение таблицы train_types_traintype
INSERT INTO train_types_traintype (type_name)
VALUES 
    ('Скоростной'),
    ('Пассажирский'),
    ('Грузовой');

-- Заполнение таблицы trains_train
INSERT INTO trains_train (train_type_id, name)
VALUES 
    (1, 'Сапсан'),
    (2, 'Ласточка'),
    (3, 'Грузовой поезд 001');

-- Заполнение таблицы positions_position
INSERT INTO positions_position (position_name)
VALUES 
    ('Машинист'),
    ('Помощник машиниста'),
    ('Кондуктор');

-- Заполнение таблицы crew_directory_crewdirectory
INSERT INTO crew_directory_crewdirectory (crew_name)
VALUES 
    ('Экипаж 1'),
    ('Экипаж 2'),
    ('Экипаж 3');

-- Заполнение таблицы personnel_personnel
INSERT INTO personnel_personnel (station_id, person_tax_id, full_name, position_id, crew_id)
VALUES 
    (1, '111111111111', 'Иванов Иван Иванович', 1, 1),
    (2, '222222222222', 'Петров Петр Петрович', 2, 2),
    (3, '333333333333', 'Сидоров Сидор Сидорович', 3, 3);

-- Заполнение таблицы routes_route
INSERT INTO routes_route (owner_station_id, train_id, departure_station_id, arrival_station_id, departure_time, arrival_time, crew_id)
VALUES 
    (1, 1, 1, 2, '2024-10-12 10:00:00', '2024-10-12 14:00:00', 1),
    (2, 2, 2, 3, '2024-10-13 12:00:00', '2024-10-13 16:00:00', 2),
    (3, 3, 3, 1, '2024-10-14 15:00:00', '2024-10-14 19:00:00', 3);

-- Заполнение таблицы route_details_routedetail
INSERT INTO route_details_routedetail (route_id, stop_number, stop_station_id, arrival_time, departure_time)
VALUES 
    (1, 1, 1, '2024-10-12 09:50:00', '2024-10-12 10:00:00'),
    (1, 2, 2, '2024-10-12 13:50:00', '2024-10-12 14:00:00'),
    (2, 1, 2, '2024-10-13 11:50:00', '2024-10-13 12:00:00'),
    (2, 2, 3, '2024-10-13 15:50:00', '2024-10-13 16:00:00'),
    (3, 1, 3, '2024-10-14 14:50:00', '2024-10-14 15:00:00'),
    (3, 2, 1, '2024-10-14 18:50:00', '2024-10-14 19:00:00');

-- Заполнение таблицы train_station (связь many-to-many между поездами и станциями)
INSERT INTO trains_train_stations (train_id, station_id)
VALUES 
    (1, 1),  -- Сапсан останавливается в Москве
    (1, 2),  -- Сапсан останавливается в Санкт-Петербурге
    (2, 2),  -- Ласточка останавливается в Санкт-Петербурге
    (2, 3),  -- Ласточка останавливается в Казани
    (3, 1),  -- Грузовой поезд 001 останавливается в Москве
    (3, 3);  -- Грузовой поезд 001 останавливается в Казани
