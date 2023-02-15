#include <stdio.h>
#include <math.h>
#define P      3
#define PI     3.141593

void pset( double x, double y )
{
  printf( "%f, %f\n", x, y );
}

void koch( void )
{
  double H, S, X, Y;        /* ORDER */
  int K, L, M, N, T[ P ];
  
  H = pow( 3, -P );
  X = 0; Y = 0; pset( X, Y );

  for ( N = 0; N < pow( 4, P ); N++ )
  {
    /***QUATERNARY NOTATION OF N***/
    M = N;
    for ( L = 0; L < P; L++ ) 
    {
      T[ L ] = M % 4;
      M = M / 4;
    }
    /***DETERMINATION SLOPE OF NTH LINE SEGMENT***/
    S = 0.0;
    for ( K = 0; K < P; K++ )
    {
      S += ( ( T[ K ] + 1 ) % 3 - 1 );
    }
    /***GRAPH OF NTH LINE SEGMENT***/
    X += cos( PI * S / 3 ) * H;
    Y += sin( PI * S / 3 ) * H;
    pset( X, Y );
  }
}

int main()
{ 
  koch();
}
