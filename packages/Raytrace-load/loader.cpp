#include <stdlib.h>  #define MAX_RAY_DEPTH 3 
 
color Trace(const Ray &ray, int depth) 
{ 
    Object *object = NULL; 
    float minDist = INFINITY; 
    Point pHit; 
    Normal nHit; 
    for (int k = 0; k < objects.size(); ++k) { 
        if (Intersect(objects[k], ray, &pHit, &nHit)) { 
            // ray origin = eye position of it's the prim ray
            float distance = Distance(ray.origin, pHit); 
            if (distance < minDistance) { 
                object = objects[i]; 
                minDistance = distance; 
            } 
        } 
    } 
    if (object == NULL) 
        return 0; 
    // if the object material is glass, split the ray into a reflection
    // and a refraction ray.
    if (object->isGlass && depth < MAX_RAY_DEPTH) { 
        // compute reflection
        Ray reflectionRay; 
        reflectionRay = computeReflectionRay(ray.direction, nHit); 
        // recurse
        color reflectionColor = Trace(reflectionRay, depth + 1); 
        Ray refractioRay; 
        refractionRay = computeRefractionRay( 
            object->indexOfRefraction, 
            ray.direction, 
            nHit); 
        // recurse
        color refractionColor = Trace(refractionRay, depth + 1); 
        float Kr, Kt; 
        fresnel( 
            object->indexOfRefraction, 
            nHit, 
            ray.direction, 
            &Kr, 
            &Kt); 
        return reflectionColor * Kr + refractionColor * (1-Kr); 
    } 
    // object is a diffuse opaque object        
    // compute illumination
    Ray shadowRay; 
    shadowRay.direction = lightPosition - pHit; 
    bool isShadow = false; 
    for (int k = 0; k < objects.size(); ++k) { 
        if (Intersect(objects[k], shadowRay)) { 
            // hit point is in shadow so just return
            return 0; 
        } 
    } 
    // point is illuminated
    return object->color * light.brightness; 
} 
 
// for each pixel of the image
for (int j = 0; j < imageHeight; ++j) { 
    for (int i = 0; i < imageWidth; ++i) { 
        // compute primary ray direction
        Ray primRay; 
        computePrimRay(i, j, &primRay); 
        pixels[i][j] = Trace(primRay, 0); 
    } 
} 
