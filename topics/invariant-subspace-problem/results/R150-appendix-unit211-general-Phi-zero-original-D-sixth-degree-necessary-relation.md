# 一般 Phi=0 整权面的原精确特化与同点 D 六次必要式

日期：2026-11-27（Asia/Taipei）  
会话：Astra-ISP-8542378f-20261127

本条完成一般 LS 中整个 $\Phi=0$ 两参数权面的第一项新原返回：原六式、两条真实歧义及同一点物理 $D$ 的三列来源均保留，得到一个必要多项式

$$
\mathcal F(u,Q,t)=0,\qquad
(\deg_u\mathcal F,\deg_Q\mathcal F,\deg_t\mathcal F)=(48,30,6).
$$

它有 $5842$ 项，总次数 $56$。所有原首项零纤维都保留；本条尚未排空该权面，也不宣称对权参数已有有限点数界。

## 1. 整个 Phi=0 面的合法原坐标

原

$$
\Phi=T_0+4u-4+Q,\qquad
T_0=2u-\ell Q-2u^2.
$$

因 $Q$ 为原单位，整个面唯一写为

$$
\ell=1-\frac{2(u-1)(u-2)}Q.
\tag{1.1}
$$

置 $v=u-1$。完整原恒等式给

$$
\ell Q=Q-2v(v-1),\qquad
T_0=-Q-4v,\qquad J-Q=-4v^2,
$$

$$
P_{02}=2v\ell Q,\qquad
\ell-u=-\frac{v(Q+2u-4)}Q.
\tag{1.2}
$$

这里只使用一般 LS 已付的原单位与整支排除。新输入还保留[整个 $Q=1-u$ 排除](R150-appendix-unit211-Q1minusU-complete-original-exclusion.md)提供的 $u+Q-1$ 单位。

源先构造[一般 LS 已付的三条完整原单首一关系](R150-appendix-unit211-general-LS-global-three-generators-over-t-and-original-unit-combination.md)，随后立即精确特化 (1.1)，才进行本面新的三列乘法及原值返回。因而没有在特化后错误重用有理函数约分前后的“分子差”规则。

令

$$
P_\ell=Q-2(u-1)(u-2),\qquad \Psi=Q\ell-P_\ell.
$$

对任一所映原多项式 $p$，取 $d=\deg_\ell p$，源构造显式几何和商 $H_p$，逐项乘回

$$
Q^d p-p_{\rm sub}=\Psi H_p.
\tag{1.3}
$$

分子、分母各按此处理。本次共 $44$ 个确定多项式映射有完整 (1.3) 检查。唯一坐标分母是原单位 $Q$，并保留原变量 $t$ 的全部有限值。

## 2. 原三列来源及物理 D

在已特化系数环 $A_\Phi[t]$ 中使用生成元 $(1,x,y)$。源实际核验：

- $x,y$ 对三个生成元的全部六列乘法及完整六原式迹；
- 原 $E_1,E_{B,e},E_{B,o},N_1,N_s,P_s$ 的三列返回；
- 两条原歧义 $x^2y$ 的两种约化、$xy^2$ 的两种约化；
- 同一点 $D_{\rm physical}=\ell(2\lambda^2-2\lambda+1)-T^2$ 的原迹。

没有假设三生成元自由或约化合流。

各原关系清分母时，只使用已付参数因子。所得三列多项式行记为 $\rho_i$；目标行记为 $d$。同一原点的生成元列为 $m=(1,x,y)^{\mathsf T}$，则

$$
\rho_i m=0,\qquad d\,m=\beta D_{\rm physical},
\tag{2.1}
$$

其中 $\beta$ 的分子、分母全是已付参数因子，故 $\beta\ne0$。实际原不同值条件给 $D_{\rm physical}\ne0$。

本次准确 QQ 小子式选择的独立原行是

$$
(E_1,N_s,P_s).
$$

其三列矩阵 $\mathcal M$ 在 QQ 有理函数域上的秩为 $3$。这是选择一个可计算原组合的依据，没有在任何实际参数点倒置 $\det\mathcal M$。

## 3. 自由三列中的完整取消与必要多项式

令 $\Delta_0=\det\mathcal M$。把第 $i$ 行替换成目标 $d$ 所得三阶行列式记为 $c_i$。源准确核验三个完整列恒等式

$$
\Delta_0d=\sum_{i=1}^3 c_i\rho_i.
\tag{3.1}
$$

随后在 $\mathbf Q[u,Q,t]$ 中取 $\Delta_0,c_1,c_2,c_3$ 的公共 gcd，全部除去后重新乘回三个自由列，得到

$$
d_0d=\sum_{i=1}^3 b_i\rho_i.
\tag{3.2}
$$

(3.2) 是全多项式身份，所以这个取消不删除公共 gcd 的零纤维。最后只从 $d_0$ 剥已付参数因子，实际得到

$$
d_0=\gamma(u,Q)\left(-\frac1{268435456}\right)\mathcal F(u,Q,t),
\tag{3.3}
$$

其中 $\gamma$ 是源中逐项乘回的已付因子乘积，且

$$
(\deg_u,\deg_Q,\deg_t)\mathcal F=(48,30,6),\quad
\deg_{\rm total}\mathcal F=56,\quad
\#\operatorname{supp}\mathcal F=5842.
$$

规范因子 $\mathcal F$ 的 SHA256 为

~~~
2ff8534ea4ed4b60cee8680d790f4d97255358edaee63e3bbd9dc19c9f66239c
~~~

源中带内容的未付必要多项式 SHA256 为

~~~
dc26b62db221e6267fe83b3138900a263b6f7824b292c0dc83eabc7171052975
~~~

把原点代入 (3.2)，由 (2.1)、$\beta\ne0$ 及 $D_{\rm physical}\ne0$ 得 $d_0=0$；再由 $\gamma\ne0$ 得 $\mathcal F=0$。这证明本文必要条件。源没有把 $\mathcal F$ 或它的 $t$ 首项当单位；所有次数下降及整纤维零条件都继续保留。

## 4. 实际执行与后续原输入

[本次自含源](../notes/2026-11-27-unit211-general-Phi-zero-original-three-column-D-return-8542.py)：

~~~
SHA256:
79bbf3491e9f6b3545e321151b9fc8f64d69fc68987fa519aed28f97ffbf2b30
Git blob:
2918d7dd9ec1412ebfd51b67ee66e80e590869b6
~~~

[小回执](../notes/2026-11-27-unit211-general-Phi-zero-original-D-sixth-receipt-8542.json)保实际 run $45980016030$ / job $140441258211$，内部 exit code 为 $0$；driver 时长 $30.687548548$ 秒，最大子进程 RSS $74212$ KiB。stdout $12028$ bytes，SHA256：

~~~
be5738240bd1f7f716969cbe51862183911e3994b014fb78b368de7be0dd12e2
~~~

实际执行及 pull 提交均为 $696b5220ab1d3663d45c6b961ec4a97eafa86d55$，两份 README blob 无变化。

本次是完整成功的原必要式计算，不是完整权面排除。后续换同一点原值输入：Phi0下由原P1及Pf单位恢复f，再由完整原N4(V)与已付bcQ·S·zeta恢复t，原W1/W2给X/Y；中心值由原两矩与物理D唯一返回。当前一般LS正是已闭L0与S0以外的L·S非零图，L=−2r·zeta且r²=1−Q为单位，故此处使用S·zeta有原依据。这个新输入将保个别N/P与所有物理条件，不分别添加只属Delta0图的E_Delta=E_C=0，也不围绕本条5842项重复扩大QQ结式；该新输入尚未执行。
