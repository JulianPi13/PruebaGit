# Implementación de Git Flow - Evidencia paso a paso

Este documento describe cronológicamente cada acción realizada en la implementación de Git Flow, explicando qué se hizo y por qué se hizo, acompañado de la evidencia correspondiente.

---

## Imagen 1

![Imagen 1](assets/Captura%20de%20pantalla%202026-03-02%20115039.png)

### ¿Qué se hizo?
Se intentó ejecutar `git flow init` después de inicializar el repositorio.

### ¿Por qué ocurrió el error?
Git no tenía configurada la identidad del usuario (`user.name` y `user.email`).  
Git Flow necesita crear ramas base y posiblemente commits internos, por lo que requiere una identidad configurada.

---

## Imagen 2

![Imagen 2](assets/Captura%20de%20pantalla%202026-03-02%20115051.png)

### ¿Qué se hizo?
Se ejecutaron los siguientes comandos:

```bash
git flow version
cd julian_pinto_gitflow
git init
git flow init
```

### ¿Por qué?
- `git flow version`: verificar que Git Flow estuviera instalado.
- `git init`: inicializar el repositorio vacío.
- `git flow init`: configurar la estructura de ramas base según Git Flow.

El proceso falló debido a la identidad no configurada.

---

## Imagen 3

![Imagen 3](assets/Captura%20de%20pantalla%202026-03-02%20115107.png)

### ¿Qué se hizo?
Se configuró la identidad global de Git:

```bash
git config --global user.email "ojulianpintou@gmail.com"
git config --global user.name "JulianPi13"
git flow init
```

### ¿Por qué?
Git necesita registrar autor y correo en cada commit.  
Sin esta configuración, no puede crear correctamente ramas ni commits.

Después de configurarlo, `git flow init` se ejecutó correctamente.

---

## Imagen 4

![Imagen 4](assets/Captura%20de%20pantalla%202026-03-02%20115849.png)

### ¿Qué se hizo?
Se creó una rama feature:

```bash
git flow feature start algoritmos
```

### ¿Por qué?
Git Flow recomienda desarrollar nuevas funcionalidades en ramas `feature/*`.  
Esto permite trabajar aislado sin afectar la rama `develop`.

La rama creada fue:
```
feature/algoritmos
```

Basada automáticamente en `develop`.

---

## Imagen 5

![Imagen 5](assets/Captura%20de%20pantalla%202026-03-02%20120155.png)

### ¿Qué se hizo?
Se desarrolló el archivo `main.py` en la rama `feature/algoritmos`.

Se observa:
- Rama activa: `feature/algoritmos`
- Ramas existentes: `develop`, `master`
- Cambios en archivos

### ¿Por qué?
El desarrollo debe hacerse en una rama feature para mantener separación entre desarrollo e integración.

---

## Imagen 6

![Imagen 6](assets/Captura%20de%20pantalla%202026-03-02%20120350.png)

### ¿Qué se hizo?
Se integró la feature a `develop`:

```bash
git checkout develop
git merge feature/algoritmos
```

### ¿Por qué?
Cuando una funcionalidad está terminada, debe integrarse a `develop`.

El merge fue tipo **fast-forward**, lo que significa que no hubo conflictos y el historial se mantuvo lineal.

---

## Imagen 7

![Imagen 7](assets/Captura%20de%20pantalla%202026-03-02%20120446.png)

### ¿Qué se hizo?
Se eliminó la rama feature:

```bash
git branch -d feature/algoritmos
```

### ¿Por qué?
Después de integrar la funcionalidad en `develop`, la rama feature ya no es necesaria.

Eliminar ramas mantiene el repositorio limpio y organizado.

---

## Imagen 8

![Imagen 8](assets/Captura%20de%20pantalla%202026-03-02%20121440.png)

### ¿Qué se hizo?
Se realizó un commit en `develop` y se creó una rama release:

```bash
git add .
git commit -m "Se crea el algoritmo en rama develop"
git flow release start v1.0
```

### ¿Por qué?
Las ramas `release/*` se crean cuando se va a preparar una versión estable del proyecto.

En este caso:
```
release/v1.0
```

Se creó basada en `develop`.

---

## Imagen 9

![Imagen 9](assets/Captura%20de%20pantalla%202026-03-02%20121603.png)

### ¿Qué se hizo?
Se verificó el historial usando el gráfico de VS Code.

### ¿Por qué?
El gráfico permite visualizar:
- Secuencia de commits
- Estructura de ramas
- Punto donde se creó la release

Esto confirma que el flujo Git Flow se aplicó correctamente.

---

## Imagen 10

![Imagen 10](assets/Captura%20de%20pantalla%202026-03-02%20123408.png)

### ¿Qué se hizo?
Se eliminó la rama release:

```bash
git branch -d release/v1.0
```

### ¿Por qué?
Después de finalizar la preparación de versión en esta práctica, la rama release ya no era necesaria.

Mantener solo `master` y `develop` ayuda a conservar orden en el repositorio.

---

# Conclusión

En esta práctica se aplicó correctamente el modelo Git Flow:

- Inicialización estructurada
- Desarrollo aislado en `feature`
- Integración en `develop`
- Creación de `release`
- Limpieza de ramas

Cada paso fue ejecutado siguiendo la metodología recomendada para control de versiones profesional.