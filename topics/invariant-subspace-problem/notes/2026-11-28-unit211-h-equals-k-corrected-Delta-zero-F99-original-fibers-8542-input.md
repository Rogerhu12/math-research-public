# 新输入：正确 $h=k,\ \Delta=0$ 的整个 $F_{99}$ 原常数纤维

日期：2026-11-28（Asia/Taipei）。本源尚未执行；不预报 $F_{99}$ 排空，不处理另一个完整 $F_{300}$ 因子。

## 1. 原范围与已成参数

工作于正确的 $h=k,\Delta=0$ 图，沿既已完整处理的碰撞坐标边界保留
$$
ABQ(1-Q)P_fbcP_{02}\,u(u-1)S\ne0.
\tag{1}
$$
这些单位必须按原碰撞和一般单位支的独立来源使用，不借已撤回的错误紧凑 $E_1$。这里物理
$D_{\rm phys}=\ell A-T^2=0$，本源任何地方都不倒它或其范数。

准确恢复为
$$
A=2\lambda^2-2\lambda+1,\quad
B=4\lambda^3-6\lambda^2+3\lambda-1,\quad
\xi=B/A,\quad
\ell=A^3/B^2,\quad T=A^2/B,
$$
$$
w=\lambda-1-T,\quad h=1+\xi,\quad
S=2\xi+3-2\lambda,\quad \eta=\xi+3-2\lambda,
$$
$$
\delta=1-Q,\quad m=u-\ell,\quad a=1-\ell,\quad
bc=(\ell^2-m^2/\delta)/4,\quad M=4bc\delta,
$$
$$
V_2=2u-\ell Q,\quad T_0=V_2-2u^2,\quad
J=2u(1-u)+\ell Q,\quad \Phi=T_0+4u-4+Q,
$$
$$
P_{02}=(2-3u)V_2-Qu+2u^3,\quad
P_f=T_0(J-Q),\quad G=\lambda P_{02}-(1-u)T_0,
$$
$$
P_c=QP_{02}(\ell+T)-GT_0,\quad
N_f=(3-4\lambda)Q+J\xi\eta,\quad
N_c=\eta(-G\xi+Qwu),
$$
$$
\Delta=\Phi N_f-S\xi P_f,\qquad
T_{\rm num}=P_fN_c-P_cN_f.
\tag{2}
$$
正确原来源给
$$
P_f f+bc\Phi z+P_c=0,\qquad
P_f NV=T_{\rm num}-bc\Delta z,\qquad z=Qt.
\tag{3}
$$
因而当前图必须同时满足 $\Delta=T_{\rm num}=0$。

已有真正 R/W/O 原 cofactor 的保留式 $F_{\rm true}(\lambda,u,Q)$，其 SHA256 为

    69babd37fc45ade649b12b4b849151574080a2bf92c7c2266141d17be1a9d999

已有独立 D/T 曲线 $P(\lambda,u)$ 的双次数为 $(28,3)$，正确新 $M(\lambda,u)$ 的双次数为 $(110,14)$。它们是同一原点的必要条件，其精确系数定义 SHA 为

    P: 8af7c105334af350ef5047ee49cf27a5aadbfa204a11b64f9b7f7b8a352dd49c
    M: 65d420e901bd60b711d76ad23699daab655414b0595383a19a93d13180f30663

固定 $u$ 结果式的已成完整权覆盖含 QQ 不可约因子 $F_{99}$。本次按已刊 coeff_profile 约定钉住唯一参数：

    e422b38e5f712eb9237d85ad116dfcdf8ec94f3886a7d97d210b48e3ce6a5a7e

既成参数来源为 Git blob $a12ac66b99fb8bc239cd303259c21a705dd02fab$。另一个 $F_{300}$ 的全部原纤维保留，不由本次任何成功或失败覆盖。

## 2. 参数再生边界与依赖

唯一新数学源码：

    2026-11-28-unit211-h-equals-k-corrected-Delta-zero-F99-original-fibers-8542.py

SHA256：

    daa2c5331f45b5583c657cbfe407660552763b65a42abda7fa379ae6b92fa005

运行时仅需两个已刊源码：

    2026-11-28-unit211-h-equals-k-corrected-Delta-zero-RWO-Q-projection-8542.py
    2026-11-28-unit211-h-equals-k-corrected-dual-germ-five-original-rows-three-cofactors-8542.py

第一文件 Git blob $4e80aedebd40af9b6bc877c0f164d69a2b13f294$，SHA256：

    3fcc2e90677b7bbd0247d72c1922fc6ed0b60da4ced715a7cecbeae656aade33

只取其读取旧 $P$ 以前的 $6055$ 字节，SHA256：

    09e0b44a9b6f244d0e2a11c1361b5382219aa5cad609efc3ae08fd370d318c7b

该前缀内部只取第二文件的原 R/W/O 必要定义 $5121$ 字节，SHA256：

    325c32cb81f37b3f31affd4e98f01c39fcee75b2cc0eae1d9cbb079edaf6d078

第二完整文件 Git blob $f33fef3b7448eb3b7d829cb7deb047706f08294d$，SHA256：

    2ea618c508489fedffdec7418cc153f6fc213ef46b329f8c55743be312d9faa2

旧独立 $P$ 仅由 runner 的终端 git 从以下固定历史输入暂取：

    ac40c96b0cfb3758fbf8bd380d18ca288a23601f:
    topics/invariant-subspace-problem/notes/2026-11-27-unit211-equal-singleton-Delta-zero-two-QQ-curves-848-base-cover-receipt-8542.json

同目录临时 basename 必须为

    isp-hk-independent-Delta-Tnum-legacy.json

工具接口不读取、传送或保存其系数载荷。新源只按上述 $P$ 的 SHA 解出相应记录，旧错误第二曲线不使用。

已成 $P,M,F_{99}$ 的定义再生采用直接 FLINT $\operatorname{Res}_u(P,M)$，按旧已付纯 $\lambda$ 支持取出同一 $F_{99}$ 并核准确 SHA。没有构造旧 $17$ 阶 Bareiss 矩阵，没有执行旧 $P/M$ gcd、旧 $722$ 点证明门、冻结的原矩阵或正目标。参数再生本身不登记为新数学成果。

## 3. 真正新增的整个常数域与同 $u$ 返回

令
$$
K=\mathbb Q[\lambda]/(F_{99,\rm monic}).
$$
保留全部 $99$ 个复嵌入，不选一个数值根。每个常数逆均通过完整 QQ 一元 Bézout，并实际返回双向乘积。

在整个 $K[u]$ 中，新计算
$$
g_u=\gcd(P,M)
$$
的完整同 $u$ Bézout。对所有实际降阶使用专门化后整个多项式，不删原 $u$ 首项为零的纤维。

若 $g_u=1$，只有此时可直接排除整个 $F_{99}$；若其次数大于 $1$，本源保留整个 $u$ 因子而结束，不增大模型。若
$$
g_u=u-u_*,
\tag{4}
$$
则它有实际原两式来源，并分别返回 $P(\lambda,u_*)=M(\lambda,u_*)=0$。所有后继都使用 $K$ 中这个唯一 $u_*$，不把模素数观测或一个复根当完整恢复。

## 4. 同一个 $Q$ 的必要理想与完整 primary 删除

在 (4) 后，将 (2) 的真实分子及 $F_{\rm true}$ 代入同一 $u_*$，在整个 $K[Q]$ 中新计算
$$
g_Q=\gcd\bigl(\operatorname{num}\Delta,
             \operatorname{num}T_{\rm num},
             F_{\rm true}\bigr).
\tag{5}
$$
每步保存并返回原三项的完整 Bézout 组合。这里只用原分子作必要条件，不倒任一新 $Q$ 首项。

仅对 (1) 中的实际原单位分子反复取 gcd。若 $d\mid g_Q$ 且 $d$ 整除原单位，则所有原点都不在 $d=0$；全部主分量通过反复整除删除，直到保留式 $q$ 与每个该单位互素。每次两次除法和累计乘积都完整返回。若某个原单位在整个 $K[Q]$ 恒为零，也可直接排该原纤维，并输出准确原单位名称。

若全部移尽或 (5) 已是 $1$，无需进入 Gram。否则只有在 $\deg_Qq\le2$ 时才继续；较高次数整因子保留。定义
$$
A_Q=K[Q]/(q_{\rm monic}),
\tag{6}
$$
不假定 (6) 为域，保留全部 $Q$ 重数。每个恢复分母必须在整个 (6) 中通过真 Bézout 逆及双向乘回；新非单位一律保留整个余因子，不换素数、复根或几何图。

## 5. 完整同 $z$ 原 Gram 八式

在 (6) 中保 $z$ 为真正原自由变量，按 (3) 和原 E0/N0 恢复
$$
f=-\frac{P_c+bc\Phi z}{P_f},\qquad
V=\frac{Jf-G+bc z}{Q},\qquad W_1=T_0/2+2uf,
$$
$$
x=\frac{(u-\ell Q)V-mW_1}{M},\qquad
y=\frac{\ell W_1-uV}{M},\qquad
t=z/Q,\qquad A_1=2f-2V+2bct.
\tag{7}
$$
附加 $\rho^2=\delta$ 仅用于保留完整偶、奇谱：
$$
b=\ell/2+\frac{m\rho}{2\delta},\quad c=\bar b,\quad
p=1+\rho,\quad q_{\rm pair}=1-\rho,\quad
X=x+\rho y,\quad Y=x-\rho y,
$$
$$
r=X-ap-ct,\qquad s_{\rm G}=Y-aq_{\rm pair}-bt.
$$
原四行保持
$$
g_0=(0,0,p,q_{\rm pair}),\quad
g_1=(0,A_1,r,s_{\rm G}),\quad
g_B=(p,r,0,t),\quad g_C=(q_{\rm pair},s_{\rm G},t,0).
$$
使用真正双点乘法
$$
v\cdot w=(v_0w_0,v_0w_1+v_1w_0,v_Bw_B,v_Cw_C),
\quad \tau(v)=av_0+v_1+bv_B+cv_C,
$$
$d=\mathcal K1,F_2=\tau(d)$ 和完整原 $N_4,P_2$。特别
$$
E_1=2\tau(g_0g_1)-2(\mathcal Kd)_1-2(d^2)_1+2F_2d_1
$$
中的 $(d^2)_1$ 严格为 $2d_0d_1$，不使用撤回的错误紧凑式。

本次八个新同 $z$ 条件为
$$
E_1,\ E_{\rm Be},\ E_{\rm Bo},\
N_4(g_0+g_1)-N_4(g_0)-N_4(g_1)-4\lambda wP_{02},
\tag{8}
$$
以及
$$
N_4(g_B)-2\lambda h^2P_{02},\qquad
P_2(g_B)-h^3P_{02}
\tag{9}
$$
的两个完整谱系数。$g_C$ 是相同原点的共轭行，两值均须为零；由于 $\rho$ 已付，(9) 的偶、奇系数同时必要。这里不把八式宣称为全原系统充分条件。

源码在 $A_Q[z]$ 中对 (8)、(9) 作原同 $z$ Bézout。每个除法只在其最高系数已在整个 $A_Q$ 中真可逆时进行。任何非单位即保留整个余纤维；只有完整八式组合真正返回 $1$，才宣称整个 $F_{99}$ 原纤维排空。若留下非恒定 $z$ 因子，则其所有根和重数仍保留。

## 6. 重数、计时和结果边界

每个 $K$ 逆的分母与 $F_{99}$ 互素；在更高 $F_{99}$ 幂的幂零增厚中，这些逆可由有限几何级数提升。原单位上的 primary 删除同样保持全重数。如果最终给出模 $F_{99}$ 的原单位身份，则任意有限 $F_{99}$ 幂厚化也由 $1+\varepsilon$ 的有限逆排除；否则本源不借幂零推新空性。

总时限 $180$ 秒、内存 $4$ GiB、外驱动 $195$ 秒；所有嵌套 alarm/setitimer 都钳在最初绝对截止，关闭计时的请求也只恢复剩余时限。资源或实现失败只记录其真实最后阶段，不增限或重放旧门。

新源只输出阶段、次数、参数 SHA 和小回执；不输出大系数、缓存或编码片。当前尚无本次 actual，整个 $F_{99}$、$F_{300}$ 和原碰撞图都不能预记排空。
