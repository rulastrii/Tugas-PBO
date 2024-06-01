-- phpMyAdmin SQL Dump
-- version 4.2.11
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Jun 01, 2024 at 02:52 AM
-- Server version: 5.6.21
-- PHP Version: 5.6.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `pbo2`
--

-- --------------------------------------------------------

--
-- Table structure for table `dosen`
--

CREATE TABLE IF NOT EXISTS `dosen` (
`id` int(11) unsigned NOT NULL,
  `nidn` varchar(100) DEFAULT '',
  `nama` varchar(100) NOT NULL,
  `bidang` varchar(100) DEFAULT ''
) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `dosen`
--

INSERT INTO `dosen` (`id`, `nidn`, `nama`, `bidang`) VALUES
(3, '333', 'Keisya', 'Ilmu Komputer'),
(25, '444', 'Lastri', ''),
(26, '555', 'Rifki', ''),
(27, '666', 'Ikoy', ''),
(28, '777', 'Rinni', ''),
(30, '999', 'Ajeng', ''),
(31, '112', 'Astry', ''),
(32, '113', 'Dian', ''),
(33, '114', 'Zaenal', ''),
(35, '116', 'Santi', ''),
(36, '117', 'Dzulkifli', ''),
(38, '500', 'Adini', '');

-- --------------------------------------------------------

--
-- Table structure for table `mahasiswa`
--

CREATE TABLE IF NOT EXISTS `mahasiswa` (
`id` int(11) NOT NULL,
  `nim` varchar(20) NOT NULL,
  `nama` varchar(100) NOT NULL,
  `tempat_lahir` varchar(100) DEFAULT NULL,
  `tanggal_lahir` date DEFAULT NULL,
  `jenis_kelamin` enum('Laki-Laki','Perempuan') DEFAULT NULL,
  `jurusan` enum('Teknik Informatika','Kimia','Olahraga','Matematika') DEFAULT NULL,
  `alamat` text,
  `gambar` varchar(255) DEFAULT NULL
) ENGINE=InnoDB AUTO_INCREMENT=59 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `mahasiswa`
--

INSERT INTO `mahasiswa` (`id`, `nim`, `nama`, `tempat_lahir`, `tanggal_lahir`, `jenis_kelamin`, `jurusan`, `alamat`, `gambar`) VALUES
(37, '220110751', 'Lastri', 'Cirebon', '2002-06-06', 'Perempuan', 'Kimia', 'Tengahtani', 'j.jpeg'),
(38, '220110752', 'Rifki', 'Palimanan', '2002-09-10', 'Laki-Laki', 'Kimia', 'Palimanan', 'h.jpeg'),
(39, '220110753', 'Rulastri', 'Cirebon', '2002-06-09', 'Perempuan', 'Kimia', 'Kalibaru', 'a.jpeg'),
(40, '220110750', 'Astry', 'Jakarta', '2000-12-12', 'Perempuan', 'Olahraga', 'Kuningan', 'i.jpeg'),
(41, '220110755', 'Ajeng', 'Kuningan', '2000-02-11', 'Perempuan', 'Teknik Informatika', 'Ngawi', 'd.jpeg'),
(42, '220110756', 'Abayansyah', 'Ciledug', '2001-12-08', 'Laki-Laki', 'Kimia', 'Cirebon', 'images.jpeg'),
(43, '220110759', 'Citra', 'Kediri', '1999-04-21', 'Perempuan', 'Teknik Informatika', 'Jakarta', 'k.jpeg'),
(44, '220110760', 'Shaquille', 'Cirebon', '1998-09-16', 'Laki-Laki', 'Teknik Informatika', 'Plered', 'download.jpeg'),
(45, '220110761', 'Zaenab', 'Cirebon', '2005-03-02', 'Perempuan', 'Olahraga', 'Plered', 'k.jpeg'),
(46, '220110767', 'Syakir', 'Bandung', '2000-12-16', 'Laki-Laki', 'Teknik Informatika', 'Cirebon', 'c.jpeg'),
(48, '220110768', 'Sulastri', 'Cirebon', '2004-10-16', 'Perempuan', 'Kimia', 'Majalengka', 'd.jpeg'),
(49, '220110769', 'Zul', 'Megu', '1997-02-01', 'Laki-Laki', 'Kimia', 'Megu', 'l.jpeg'),
(52, '220110770', 'Vasya', 'Cirebon', '2005-08-06', 'Perempuan', 'Matematika', 'Kedawung', 'g.jpeg'),
(53, '220110778', 'Tesya', 'Majalengka', '2000-09-02', 'Perempuan', 'Matematika', 'Bandung', 'f.jpeg'),
(56, '220110780', 'Sasya', 'Malang', '2000-08-09', 'Perempuan', 'Kimia', 'Cirebon', 'a.jpeg'),
(58, '209817', 'Jingga', 'UN', '1223-12-12', 'Laki-Laki', 'Teknik Informatika', 'J', 'download.jpeg');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `dosen`
--
ALTER TABLE `dosen`
 ADD PRIMARY KEY (`id`), ADD UNIQUE KEY `nim` (`nidn`);

--
-- Indexes for table `mahasiswa`
--
ALTER TABLE `mahasiswa`
 ADD PRIMARY KEY (`id`), ADD UNIQUE KEY `nim` (`nim`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `dosen`
--
ALTER TABLE `dosen`
MODIFY `id` int(11) unsigned NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=39;
--
-- AUTO_INCREMENT for table `mahasiswa`
--
ALTER TABLE `mahasiswa`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=59;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
