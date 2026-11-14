# R168：原循环二次量与同一 Heegner 配对的 p 进高度变化

日期：2026-11-12。**已证明；无穷非零仍未证明。**
[完整证明与规范](../notes/2026-11-12-cyclic-energies-as-heegner-height-variation.md)。

保留原 $R=D_pQ$、全部 p 完成和
$z=\log_E(R)/p$。对
$$
 K_r=\sum_{d=0}^{p-1}\{d(p-d)\}^r\tau^d,\qquad r=1,2,
$$
R161/R164 的实际对数二次量为
$\mathcal E_r(z)=\operatorname{Tr}_{L/F}(zK_rz)/(2r)!$。

按 Coleman–Gross 杯积方向
$[\eta_0]\cup[\omega]=1$，
把 Hodge 补空间改为
$W_\lambda=\mathbb Q_p[\eta_0+\lambda\omega]$。
Balakrishnan–Besser（2015）Theorem 4.1 及 polarization 给
$$
 \Delta_\lambda h^{\rm pre}_v(P,Q)
                  =-\lambda\log_E(P)\log_E(Q).
$$
使用未除以数域次数的 cyclotomic 全局高度，
在所有 p 完成采用同号 $\lambda$，则
$$
 \boxed{\displaystyle
 \mathcal E_r(z)=
 -\frac{h^L_\lambda(R,K_rR)-h^L_0(R,K_rR)}
                   {2\lambda p^2(2r)!}.}
$$
这里的 2 来自 $F/\mathbb Q$ 的迹；
两 split 完成的同号变化保持复共轭。

若 $V_0=C_\ell\times U$、$|V_0|=h_Fu=[H_\ell:L]$，
则分子准确为
$$
 \frac{t_0^2}{h_Fu}
 \sum_{a,b\in V_0}\sum_d\{d(p-d)\}^r\,
 \Delta_\lambda h^{H_\ell}
       (D_pP_\ell^a,D_pP_\ell^{b\tau^d}).
$$
因此原双重全迹与循环权没有丢失。

原 newform 商和 Hecke 作用进一步给固定 weight 2 级数
$$
 -\frac{\mathcal Z_{r,\lambda}-\mathcal Z_{r,0}}
                    {2\lambda p^2(2r)!}
                      =\mathcal E_r(z)\,f .
$$
这是合法的二次 lift，R165 的线性 heart 界不适用。
但它仍是未知标量乘 f，尚无独立单位 Fourier 系数。
Disegni（2017）的 Gross–Zagier 高度采用规范 ordinary 分裂，
不能未经比较同时套到任意 $W_\lambda$ 后相减。

依赖：R130、R139、R154、R157、R161、R164；
主来源与全部局部、全局常数见完整证明。
