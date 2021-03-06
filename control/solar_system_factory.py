import solarsystem
import sun
import planet
import moon

from random import randint

class SolarSystemFactory():
    
    def create_sol(self):
        m_solarsystem = solarsystem.SolarSystem(sun.Sun()) 
        m_solarsystem.add_planet(planet.PlanetFactory.create_mercury(), 5.7909e10) 
        m_solarsystem.add_planet(planet.PlanetFactory.create_venus(), 1.0816e11)
        m_solarsystem.add_planet(planet.PlanetFactory.create_earth(), 1.496e11)
        m_solarsystem.add_planet(planet.PlanetFactory.create_mars(), 2.22799e11)
        m_solarsystem.add_planet(planet.PlanetFactory.create_jupiter(), 7.7836e11)
        m_solarsystem.add_planet(planet.PlanetFactory.create_saturn(), 14.335e11)
        m_solarsystem.add_planet(planet.PlanetFactory.create_uranus(), 28.724e11)
        m_solarsystem.add_planet(planet.PlanetFactory.create_neptun(), 44.95e11)
        return m_solarsystem

    @staticmethod
    def create():
        m_solarsystem = solarsystem.SolarSystem(sun.SunFactory.create())
        m_planet_count = randint(0,15)

        for i in range(0, m_planet_count): 
            m_planetarysystem = PlanetarySystemFactory.create()
            m_distance =  randint(5.79e10, 44.95e11)
            m_solarsystem.add_planet(m_planetarysystem, m_distance)

        return m_solarsystem

class PlanetarySystemFactory():
    
    @staticmethod
    def create():
        m_planet = planet.PlanetFactory.create()
        m_planetarysystem = planet.PlanetarySystem(m_planet) 
        m_planet = m_planetarysystem.center 
        m_moon_count = randint(0,40)

        for j in range(0, m_moon_count):
            m_orbit = randint(m_planet.diameter * 2 ,m_planet.diameter * 100)
            m_moon = moon.Moon(randint(3, 40000), m_orbit)
            m_planetarysystem.add_orbiting_object(m_moon, randint(5.79e3, 44.95e5))

        return m_planetarysystem

