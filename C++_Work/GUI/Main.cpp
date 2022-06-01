// for initializing and shutdown functions
#include <SDL2/SDL.h>
 // for rendering images and graphics on screen
#include <SDL2/SDL_image.h>
 // for using SDL_Delay() functions
#include <SDL2/SDL_timer.h>
#include <SDL2/SDL_ttf.h>
#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <string>
#include <iostream>
#pragma comment(lib, "user32.lib")
using namespace std;

#define PI 3.14159265358979323f
int nb_Frame = 0;
bool isFullScreen = true;

void toggleFullScreen(SDL_Window* window){
    isFullScreen = !isFullScreen;
    if (!isFullScreen){
        SDL_DisplayMode DM;
        SDL_GetCurrentDisplayMode(0, &DM);
        auto Width = DM.w;
        auto Height = DM.h;
        SDL_SetWindowSize(window,Width,Height);
    }
    else SDL_SetWindowSize(window,800,800);
    SDL_SetWindowFullscreen(window, !isFullScreen);
}

// mettre en place des ancres haut, bas ...
// mettre en place un système d'objet plus tard, utilisation provisoire de variable global
//faire des widgets une fois que 500 lignes atteints
//faire l'animation d'arc de cercle en rotation
float getAngle(int x, int y){
    return PI-atan2(y,x);
}

void DrawArcCircle(SDL_Renderer *renderer, int x, int y, int radius, int thick, int begin = 0, int ending = 359){
    int rad = (radius-thick)*(radius-thick);
    begin%=360,ending%=360;
    float beg = begin * PI / 180, end = ending * PI / 180;
    if (ending<begin){
        DrawArcCircle(renderer,x,y,radius,thick,begin);
        DrawArcCircle(renderer,x,y,radius,thick,0,ending);
    }
    else{
        for (int w = 0; w < radius * 2; w++){
            for (int h = 0; h < radius * 2; h++){
                int dx = (float)radius - w, dy = (float)radius - h, res = dx*dx + dy*dy;
                float point_angle = getAngle(w-radius,h-radius);
                if (res <= radius*radius && res>rad && point_angle<=end && beg <= point_angle)
                    SDL_RenderDrawPoint(renderer, x + dx, y + dy);
            }
        }
    }
    
}

void DrawCircle(SDL_Renderer *renderer, int x, int y, int radius, int thick){
    for (int w = 0; w < radius * 2; w++){
        for (int h = 0; h < radius * 2; h++){
            int dx = radius - w,dy = radius - h,res = dx*dx + dy*dy, rad = radius-thick;
            if (res <= radius*radius && res>rad*rad) SDL_RenderDrawPoint(renderer, x + dx, y + dy);
        }
    }
}

void DrawFillCircle(SDL_Renderer *renderer, int x, int y, int radius){
    for (int w = 0; w < radius * 2; w++){
        for (int h = 0; h < radius * 2; h++){
            int dx = radius - w,dy = radius - h;
            if ((dx*dx + dy*dy) <= (radius * radius))
                SDL_RenderDrawPoint(renderer, x + dx, y + dy);
        }
    }
}

void DrawLine(SDL_Renderer * renderer, int x1, int y1, int x2, int y2, int thick){
    //ajouter en fonction de la taille de la zone (hauteur ou largeur)
    if (x1-x2>y1-y2) for (int i = 0; i < thick; i++) SDL_RenderDrawLine(renderer,x1+i, y1, x2+i, y2);
    else for (int i = 0; i < thick; i++) SDL_RenderDrawLine(renderer,x1, y1+i, x2, y2+i);
}

// surcharger le constructeur avec une option de proportion et de hauteur/largeur
void Image(SDL_Renderer* renderer, string path, int x, int y){
    SDL_Texture* Message = SDL_CreateTextureFromSurface(renderer, IMG_Load( path.c_str() ));
    int texW = 0,texH = 0;
    SDL_QueryTexture(Message, NULL, NULL, &texW, &texH);
    SDL_Rect mesRect = { x, y, texW, texH };
    SDL_RenderCopy(renderer, Message, NULL, &mesRect);
}

SDL_Rect Text(SDL_Renderer *renderer, const string &txt, int x, int y,int size){
    TTF_Font* police = TTF_OpenFont("Ubuntu/Ubuntu-Regular.ttf", size);
    if (!police) {
        printf("TTF_OpenFont: %s\n", TTF_GetError());
    }
    SDL_Color Blue = {50, 150, 250};
    SDL_Surface* surfaceMessage = TTF_RenderText_Blended(police, txt.c_str(), Blue);
    SDL_Texture* Message = SDL_CreateTextureFromSurface(renderer, surfaceMessage);
    int texW = 0,texH = 0;
    SDL_QueryTexture(Message, NULL, NULL, &texW, &texH);
    SDL_Rect mesRect = { x, y, texW, texH };
    SDL_RenderCopy(renderer, Message, NULL, &mesRect);
    TTF_CloseFont(police);
    return mesRect;
}

void ListFuturiste(SDL_Renderer *rend, int x, int y, const vector<string> &liste){
    SDL_SetRenderDrawColor(rend, 50,150,250,0);
    int Mx, My; SDL_GetMouseState(&Mx, &My);
    int sizettf = 14, sizecircle = 2, lisize = liste.size(), separation = 18;
    for (int i = 0; i < lisize; i++){
        DrawFillCircle(rend, x+separation/2,y+(i+0.5)*separation,sizecircle);
        SDL_Rect rect = Text(rend,liste[i],x+separation,y+(i+0.5)*separation-(sizettf+sizecircle)/2,sizettf);
        if (rect.x-10 <= Mx && Mx <= rect.x+rect.w && rect.y <= My && My <= rect.y+rect.h){
            int deg = nb_Frame*4;
            DrawArcCircle(rend,x+separation/2,y+(i+0.5)*separation, 6,2,deg,80+deg); deg += 120;
            DrawArcCircle(rend,x+separation/2,y+(i+0.5)*separation, 6,2,deg,80+deg); deg += 120;
            DrawArcCircle(rend,x+separation/2,y+(i+0.5)*separation, 6,2,deg,80+deg);
        }
    }
    int end = y+(lisize-0.2)*separation;
    DrawLine(rend,5, y, 5, end,2); DrawLine(rend,5, end, 5+separation/1.5, end+separation/2,2);
}

void DNAverticale(SDL_Renderer *renderer, int x, int y, int width, int height, int radius, int avance){
    for (float h = 0; h < height; h++){
        int sinus = (sin((h+avance)/20)+1)*width+radius,
        sinus2 = (sin((h+avance)/20+PI)+1)*width+radius;
        bool first = sinus>(sin((h+avance-2)/20)+1)*width+radius;
        if (first) radius += 15;
        for (float w = sinus-radius; w < sinus; w++){
            SDL_RenderDrawPoint(renderer, x+w, y+h);
        }
        if (!first) radius += 15;
        for (float w = sinus2-radius; w < sinus2; w++){
            SDL_RenderDrawPoint(renderer, x+w, y+h);
        }
        radius-=15;
        if ((int)(h/(radius/2))%2==0){
            if (sinus2 < sinus){
                int savesin = sinus;
                sinus = sinus2;
                sinus2 = savesin;
            }
            if (sinus2-sinus>30){
                uint8_t r,g,b,a; SDL_GetRenderDrawColor(renderer,&r,&g,&b,&a);
                SDL_SetRenderDrawColor(renderer, r-50,g-50,b-50,a);
                for (float w = sinus-radius/2; w < sinus2-radius/2; w++){
                    SDL_RenderDrawPoint(renderer, x+w, y+h);
                }
                SDL_SetRenderDrawColor(renderer, r,g,b,a);
            }
        }
    }
}

void Info(SDL_Renderer *renderer,int h){
    //SDL_GetWindowData
    string text = "";
    Text(renderer,text,0,h-140,14);
}

uint8_t main_loop(SDL_Renderer* rend, SDL_Window* win){
    uint8_t close = 0;
    //event
    SDL_Event event;
    while (SDL_PollEvent(&event)) {
        switch (event.type) {
            case SDL_QUIT: close = 1; break;
            case SDL_KEYDOWN:
                switch (event.key.keysym.scancode) {
                    case SDL_SCANCODE_F11:toggleFullScreen(win); break;
                    default:break;
                }
        }
    }
    //affichage
    SDL_RenderClear(rend);
    vector<string> liste = {"Visual Scripting","Modelisation 3D","Image","Son","Moteur de jeu"};
    ListFuturiste(rend,5,0,liste); 

    nb_Frame++; if (nb_Frame>=1000) nb_Frame %= 314;
    DNAverticale(rend,0,200,50,200,15,nb_Frame*1.5);

    int x, y, w, h; SDL_GetMouseState(&x, &y); SDL_GetWindowSize(win, &w, &h);

    int deg = nb_Frame*2;
    DrawArcCircle(rend,200,200, 60,15,deg,80+deg); deg += 120;
    DrawArcCircle(rend,200,200, 60,15,deg,80+deg); deg += 120;
    DrawArcCircle(rend,200,200, 60,15,deg,80+deg);

    Image(rend,"World_map_-_low_resolution.svg",200,10);

    Info(rend,h);
    Text(rend,to_string(x)+"/"+to_string(w)+" : "+to_string(y)+"/"+to_string(h),0,h-14,14);
    return close;
}

int main(int argc, char *argv[]){
    if (SDL_Init(SDL_INIT_EVERYTHING) != 0)
        printf("error initializing SDL: %s\n", SDL_GetError());
    TTF_Init();
    SDL_SetHint( SDL_HINT_RENDER_SCALE_QUALITY, "1" );
    SDL_GL_SetAttribute(SDL_GL_MULTISAMPLEBUFFERS, 1);
    SDL_GL_SetAttribute(SDL_GL_MULTISAMPLESAMPLES, 8);
    SDL_GL_SetAttribute(SDL_GL_ACCELERATED_VISUAL, 1); 
    SDL_Window* win = SDL_CreateWindow(
        "Launcher - AlphaSoftware", SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED, 800, 800, 0);
    SDL_SetWindowResizable(win, SDL_TRUE);
    
    Uint32 render_flags = SDL_RENDERER_ACCELERATED;
    SDL_Renderer* rend = SDL_CreateRenderer(win, -1, render_flags);
    uint8_t close = 0;
    while (close%2==0){
        close = main_loop(rend,win);
        SDL_SetRenderDrawColor(rend,20,20,20,0);
        SDL_RenderPresent(rend);
        SDL_Delay(1000 / 70);//70 FPS
    }
    SDL_DestroyRenderer(rend);SDL_DestroyWindow(win);TTF_Quit();SDL_Quit();return 0;
}
