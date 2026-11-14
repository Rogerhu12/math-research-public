# R174. 整形式 Cartan 坐标与实际共同前缀矩阵

**状态：已证明。** 日期：2026-11-12。

完整证明：
[真实 CM 的整形式 Cartan 作用与同一混合前缀矩阵](../notes/2026-11-12-actual-cm-formal-cartan-and-common-prefix-matrix.md)。

固定 R167 的 $a=\vartheta^4$、$b=\sigma^4$、$w=z^4$。
对惰性 $p\ge7$，令
$r=(p+1)/4$、$R=(p^2-1)/4$。

## 全精度整作用

R170 的每个固定阶环境 jet 系数是 $\beta^4,N\beta$ 的固定有理
多项式。沿 Gaussian 整数取逐系数极限，实际 CM 多项式作用延拓为
$\mathbb Z_p[i]$ 上的整形式作用。
其中 $\mu_{p^2-1}/\mu_4$ 是阶 $R$ 的真实有限群。

分别对横向角色 $\alpha^{p+1}$ 和切向角色 $\alpha^4$ 作平均，
得到整形式坐标

$$
U=a-1-b/3+O((a-1,b)^2),\qquad
V=b+O((a-1,b)^2).
$$

它们及整逆实际定义在 $\mathbb Z_p$ 上。
沿原曲线、再以 $v=V(w)$ 为输出后，

$$
U=v^r g(v^R),\qquad v_p(g(0))=-1.
$$

故在 $k<pr$ 的完整区间内，
$U=g(0)v^r\pmod{v^{pr}}$；这不是只在模 $p$ 的一次近似。

## 同一个原源上的行与尾

对 $E_D=\mathbb Z_p[a-1,b]_{\le D}$，用同一个整形式逆写

$$
\widetilde P(U,V)=\sum L_{\ell,j}(P)U^\ell V^j,\qquad
\|L_{\ell,j}\|_p\le1.
$$

令 $u_0=g(0)$、$\pi_0=u_0^{-1}\in p\mathbb Z_p^\times$。
对 $k=rh+j<pr$、$0\le j<r$，真实行准确为

$$
[v^k]P(\gamma_v)
=u_0^h\Lambda_{h,j}(P),\qquad
\Lambda_{h,j}
=\sum_{q=0}^{h}\pi_0^q L_{h-q,j+rq}.
$$

这些共同整行是对单首一式 $V^r-\pi_0U$ 作形式除法所得的余式
系数。全部先前零行条件必须一并保留；真实范数是
$p^h$ 乘 $\Lambda_{h,j}$ 在该饱和核上的像理想范数。

总次数 $>D$ 的形式源尾在第 $k$ 行的范数至多

$$
p^{\min\left(\lfloor k/r\rfloor,\,
 \lfloor(k-D-1)/(r-1)\rfloor\right)}
\quad(D<k<pr).
$$

低次环境 Taylor 矩阵虽整可逆，高次尾一般仍存在。
本文未把形式 Cartan 坐标当作原 $E_D$ 上的免费
$\mathrm{GL}(E_D)$ 变换，也未从裸共振个数扣减 R159 的预算。
