#include <stdio.h>
#include <math.h>
#define PI     3.141593

void pset( double x, double y )
{
  printf( "%f, %f\n", x, y );
}

void mira( void )
{
  double A, B, C, X, Y, Z, U, W;
  int N, P;

  A = 0.7; B = 0.9998; P = 12000; C = 2 - 2 * A;
  X = 0.0; Y = 12.1;

  W = A * X + C * X * Y / ( 1 + X * X );
  for ( N = 0; N <= P; N++ )
  {
    if ( N > 100 ) { pset( X, Y ); }
    Z = X; X = B * Y + W; U = X * X;
    W = A * X + C * U / ( 1 + U );
    Y = W - Z;
  }
}

int main()
{ 
  mira();
}
