# PuertaPerruna V2

Esta es la versión 2 del sistema PuertaPerruna, que implementa un sistema de monitoreo de estados utilizando el patrón Observador.

## Características

- Monitoreo en tiempo real de múltiples puertas
- Dashboard con estadísticas de estado
- Detección y manejo de errores
- Sistema de reparación automática

## Estructura del Proyecto

- `observador.py`: Define las interfaces del patrón Observador y los estados posibles
- `puerta_perruna.py`: Implementa la lógica de la puerta con el patrón Observable
- `dashboard.py`: Implementa el observador que muestra las estadísticas
- `simulador.py`: Script para simular el funcionamiento del sistema

## Estados de la Puerta

- **ABIERTA**: La puerta está abierta
- **CERRADA**: La puerta está cerrada
- **ERROR**: La puerta ha tenido un fallo y necesita reparación

## Uso

Para ejecutar la simulación:

```bash
python simulador.py
```

## Características de Seguridad

- Detección de errores consecutivos
- Límite de intentos antes de entrar en estado de error
- Sistema de reparación para recuperar puertas en estado de error

## Monitoreo

El dashboard muestra:
- Conteo total de puertas en cada estado
- Estado actual de cada puerta individual
- Actualizaciones en tiempo real 