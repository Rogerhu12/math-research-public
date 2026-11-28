# W 的 alpha 零整支：完整原 f/t 恢复及单 V 新输入

日期：2026-11-28（Asia/Taipei）。会话 Astra-ISP-8542378f-20261127。

这是整个当前 W 的 $t=0$、$f=u$ 已闭之后的新输入。
完整 Python 源 2026-11-28-unit211-W-alpha-zero-whole-original-single-V-projections-8542.py 尚未执行；15909 字节，SHA256 87abb760a803666ff0ec1e8afeb8c7bdc7737d908b5b8d56625856ad04a2cc61。首次界 180 秒 / 4 GiB，零文件依赖。
不重跑旧 t0、fu、任何旧 determinant 或模返回。

## 1. 整个 alpha 零支的原恢复

设
$$
\delta=1-Q,\quad m=u-\ell,\quad V_2=2u-\ell Q,\quad
T_0=V_2-2u^2,\quad M=\ell V_2-u^2=4bc\delta,
$$
$$
\widehat U=u-\ell Q,\qquad \eta=f-u,\qquad
\alpha=4\delta\eta-\widehat U t,\qquad V=bX+cY.
$$
原 $E_0$ 给 $W_1=bpX+cqY=(T_0+4uf)/2$，故
$$
x=\frac{\widehat U V-mW_1}{M},\qquad
y=\frac{\ell W_1-uV}{M}.
\tag{1}
$$
只除已付 $M$。真正原均值差的正确 $R_{\rm true}$ 满足
$$
\begin{aligned}
\delta R_{\rm true}
={}&\alpha V+\frac M4t^2+Mu\,t
 +\frac m2t(T_0+4uf)-4\delta f(f-u),\\
E_1-EW={}&-2R_{\rm true}.
\end{aligned}
\tag{2}
$$
这里 $R_{\rm true}$ 采用除去原 $Q^2$ 的记号；若使用旧 compact 定义，其值为本式的 $Q^2$ 倍。源码直接返回原均值差，未混用两种尺度。

在整个 $\alpha=0$ 上，由已付 $t$ 得
$$
f=u+\frac{\widehat U t}{4\delta}.
$$
令
$$
R_w=2u(1-u)-uQ+(2u-1)\ell Q,\quad
A_\alpha=M\delta+\{2u(u-\ell)-\widehat U\}\widehat U.
$$
完整原恒等式是
$$
4\delta^2 R_{\rm true}
=t\{A_\alpha t-2\ell\delta R_w\}.
\tag{3}
$$

代当前 W 权坐标
$$
u=e+1,\quad Q=ek,\quad V_b=uk+2,\quad
\ell=\frac{u((k+2)^2-2ek)}{kV_b},\quad
H=4ek-k^2-4k-8
$$
后，准确有
$$
R_w=-\frac{e^2uH}{V_b},\qquad
\boxed{A_\alpha=\frac{e^2u^2(k+2)H(Q-2)}{kV_b^2}.}
\tag{4}
$$
这些因子全部是已付当前 W 权单位，特别 $Q-2$ 和 $k+2$ 来源于整个等权排除。因而本次不留下一个未支付的 $A_\alpha=0$ 曲线；整个 $\alpha=0$ 必须具有唯一
$$
\boxed{
t=-\frac{2\delta((k+2)^2-2Q)}{(k+2)(Q-2)},\qquad
f=u+\frac{\widehat U t}{4\delta}.
}
\tag{5}
$$
由 $\alpha=0$ 和已付 $t(f-u)$，$\widehat U$ 亦在本支成为单位。这个支付仅用于本支；它不外推到全部 W。

(4) 的新纯权多项式乘法已实际 5 ms 返回，剥 $e^2ku^2(k+2)H$ 后恰为 $Q-2$；完整新原均值/N/P 源尚未执行。源码会从 (1)、(5) 的同一个 Gram 直接核原 $E_0,N_0,P_0,P_1$、$E_1=EW$ 和全部 $N/P$，不把这项小参数返回说成完整原系统已返。

## 2. 原均值的一次组合及新的两条低值行

(1)、(5) 只有一个自由几何坐标 $V$。$EW$、$EBo$ 对 $V$ 至多二次，其平方头分别为
$$
-\frac{2V_2}{M},\qquad \frac{4u\widehat U}{M^2}.
$$
因此完整原组合
$$
L_m=2u\widehat U\,EW+MV_2\,EBo
\tag{6}
$$
至多对 $V$ 一次；没有倒其一次头或常数项。

使用新一般自由 $f,t$ weighted/jet 身份。记 $\sigma=2$、
$S_x=X+Y$、$P_x=pX+qY$，并沿同一点定义
$$
\begin{aligned}
K_w=2\{&t^2+(5u-2S_x-2)t+2XY+2P_x-2uS_x\\
&+2u^2-6u+Q\},
\end{aligned}
$$
$$
\begin{aligned}
K_\lambda=2\{&t^2+2(3u-S_x-2)t+2XY+3P_x+(2-2u)S_x\\
&-2W_1+4u^2-16u+4+\ell Q\}.
\end{aligned}
$$
两个新原低行是
$$
L_w=2P_{02}(2\lambda-1)(\lambda-1-T)
-bc\,t\{K_w+4(f-u)(t-2)\},
$$
$$
L_\lambda=2P_{02}\lambda(2\ell-1)-4u(f-u)A_1
-bc\,t\{K_\lambda+4(f-u)(t-4)\}.
$$
在本次同原 $E_0,N_0,P_1$ 恒等恢复下，源码完整核
$$
\boxed{L_w=NS-PS+E_{W,2},}
$$
$$
\boxed{L_\lambda=NS-PS+N_1+E_{W,2}+2E_p-2uE_1,}
\tag{7}
$$
其中 $E_{W,2}=b(2p-u-X)E_B+c(2q-u-Y)E_C$、
$E_p=bpE_B+cqE_C$。两低行对 $V$ 至多二次。

后继必要行选择 $N_1,L_w,NS$。在原均值上，它们保留整个 $NS,PS$，而非任意抛弃一个 weighted 条件；$L_\lambda$ 的完整身份也核回，但不把它计作独立新条件。

## 3. 首项零和垂直分量的完整保留

先完整返回所有有理原行，只清已付权分母/内容。纯权必要式优先取 (6) 在恰为常数行时的原常数，否则取固定 $\operatorname{Res}_V(EW,EBo)$。

若纯权式非零而非常数，先用固定 $\operatorname{Res}_V(L_m,N_1/L_w/NS)$。若仍有共同曲线，再加入以 $EW,EBo$ 为第一行的六个固定原结式。新 $V$ 一次/二次头零始终保留。常数对常数的退化不会误返回空的 Sylvester 行列式 1：源码保第一条原常数必要式。

多变量 gcd 仅用来判断是否存在共同曲线；非恒定时保整个共同曲线，不判空。
若 gcd 为常数，则选择两个真实原组合 $\sum c^jR_j$，分别作固定 e 结式。选择界用纯权式的**总次数**，包括所有垂直 k 分量，不假定其 e 首项为单位。
若两式都是 e 常数，也保原 k 必要式，不把 0 阶行列式 1 当排空证据。

最终只剥当前已付 $k,k+1,k+2,k+4$ 后，做真正 $\mathbb Q[k]$ 两乘回 Bézout。唯实际常数覆盖才闭整 $\alpha=0$；否则保存全部剩余因式/重数的定义、度与 SHA，下一换真正原有限输入。所有资源边界按真实 checkpoint 登记。

整个 $\alpha=0$ 若关闭，互补图即可将原 (2) 对 $V$ 唯一求解，减少剩余全 W 的几何变量。现在没有预先宣称这一支已空。
