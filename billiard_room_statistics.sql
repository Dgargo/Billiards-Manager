-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Хост: 127.0.0.1
-- Время создания: Июн 23 2021 г., 20:02
-- Версия сервера: 10.4.18-MariaDB
-- Версия PHP: 8.0.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `billiard_room_statistics`
--

-- --------------------------------------------------------

--
-- Структура таблицы `main_info`
--

CREATE TABLE `main_info` (
  `id` int(3) NOT NULL,
  `orderdate` date NOT NULL,
  `ordertime` time NOT NULL,
  `countHours` int(2) NOT NULL,
  `numberTable` int(1) NOT NULL,
  `revenue` int(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_estonian_ci;

--
-- Дамп данных таблицы `main_info`
--

INSERT INTO `main_info` (`id`, `orderdate`, `ordertime`, `countHours`, `numberTable`, `revenue`) VALUES
(1, '2021-06-23', '21:00:34', 1, 1, 100);

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `main_info`
--
ALTER TABLE `main_info`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `main_info`
--
ALTER TABLE `main_info`
  MODIFY `id` int(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
