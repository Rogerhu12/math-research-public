# h=k：修正二重点乘法后的五条原行与三个完整标量组合

日期：2026-11-28（Asia/Taipei）。会话 Astra-ISP-8542378f-20261127。
AI-assisted，GPT-6 Astra Pro。

源 `2026-11-28-unit211-h-equals-k-corrected-dual-germ-five-original-rows-three-cofactors-8542.py`。
SHA256 `2ea618c508489fedffdec7418cc153f6fc213ef46b329f8c55743be312d9faa2`；
11368 字节。自含、无文件依赖，首次预算 180 秒 / 4 GiB。
尚未执行，下面只给新输入、原身份与实际目标。

## 1. 真正的原坐标图

原 h=k 值条件中记
$$
A=2\lambda^2-2\lambda+1,\quad
B=4\lambda^3-6\lambda^2+3\lambda-1,
$$
$$
\xi=B/A,\quad \ell=A^3/B^2,\quad T=A^2/B,\quad
h=1+\xi,\quad w=\lambda-1-T.
$$
本源仅工作在明确的
$$
ABQ(1-Q)P_f\ne0
$$
坐标图。没有从已撤回的紧凑式借用任何头或权面排除；
A/B/Pf 的零面不因本次坐标选择被宣布关闭。

令 $\delta=1-Q$、$m=u-\ell$、$a=1-\ell$，
$$
bc=(\ell^2-m^2/\delta)/4,\quad
V_2=2u-\ell Q,\quad T_0=V_2-2u^2,\quad
J=2u(1-u)+\ell Q,
$$
$$
\Phi=T_0+4u-4+Q,\quad
P_{02}=(2-3u)V_2-Qu+2u^3,\quad
P_f=T_0(J-Q),\quad
G=\lambda P_{02}+(u-1)T_0,
$$
$$
P_c=QP_{02}(\ell+T)-GT_0,\quad
z=Qt,\quad f=-(P_c+bc\Phi z)/P_f,\quad
v_n=Jf-G+bc z,\quad V=v_n/Q.
$$
$f,V$ 始终是同一组原 Gram 的坐标。$\Delta$ 完全不倒置，保留整个零纤维。

## 2. 原 P1 与完整 N(V) 的独立恢复

这里重新给出不依赖错误 E1 的原来源，防止只沿旧 compact 名称传递必要性。

原 Gram 四行为
$$
(0,0,p,q),\quad(0,A_1,r,s),\quad(p,r,0,t),\quad(q,s,t,0),
$$
其中
$$
p=1+\rho,\quad q=1-\rho,\quad \rho^2=\delta,\quad
A_1=2f-2V+2bc\,t,\quad r=X-ap-ct,\quad s=Y-aq-bt.
$$
原 $E_0=0$ 给 $2W=T_0+4uf$，$W=bpX+cqY$。
原 $N_4(g_0)=2\lambda P_{02}$ 给
$v_n=Jf-G+bc z$。这些恒等式只使用原二重点乘法。

原中心化极化三次迹 $P_j=3\tau((g_0-u1)^2(g_1-\tau(g_1)1))$ 满足
$$
P_j/3=2\ell Q f+(T_0-Q)V+(1-u)T_0-aP_{02}
       +bc(4u-4+2Q)t.
$$
因此直接代入上述同一点恢复式得到
$$
\boxed{Q(P_j/3-wP_{02})=P_ff+P_c+bc\Phi z=0.}
$$
这是完整原 P1；源对这整个仿射 $z$ 恒等式实际相减检查。

在 h=k 上原值向量为 $\mathcal V=(1,w,h,h)$。
$AB\ne0$ 下的参数给
$$
\tau(\mathcal V)=\lambda,\quad
\tau(\mathcal V^2)=2\lambda^2,\quad
\tau(\mathcal V^3)=4\lambda^3.
$$
原 $d=DK(1)=(u,2f-V-au,X,Y)$，所以按真实 jet 乘法：
$$
\tau(d\mathcal V)=2f+uw+\xi V,
$$
$$
\tau(d\mathcal V^2)=2f+2uw+(2\xi+\xi^2)V,
$$
$$
\tau(\mathcal V DK(\mathcal V))
=2f+2\xi V+2(1+\xi)uw+2bc\xi^2t.
$$
完整原 $N_4$ 由此给
$$
\frac Q2N_4(\mathcal V)
=N_F f+bc S\xi z+N_C=:\mathcal N_V,
$$
$$
N_F=(3-4\lambda)Q+J\xi(\xi+3-2\lambda),\quad
S=2\xi+3-2\lambda,\quad
N_C=(\xi+3-2\lambda)(-G\xi+Qwu).
$$
源实际检查这个完整 $N_4$ 身份。没有用只在未付几何余式为零时成立的投影替代它。
再置
$$
\Delta=\Phi N_F-S\xi P_f,\qquad
T_{\rm num}=P_fN_C-P_cN_F.
$$
于是准确有
$$
P_f\mathcal N_V=T_{\rm num}-bc\Delta z.
$$

## 3. 修正后的五行与原理想标量

首条必须使用已完成的七变量整数证书
`2026-11-28-unit211-corrected-dual-germ-compact-original-identities-8542.js`
（SHA256 `a7f1db4305a58c2e733c573158f746d5b4adc312090472de25e472c96ddfeaae`）：
$$
R_{\rm true}=
4Q(f-u)(v_n-Qf)+bc z^2+z(4bc uQ-\ell v_n)
+\frac{m}{2\delta}z\{Q(T_0+4uf)-2v_n\}.
$$
另取独立正确的 $W_4/(4\delta)$、$O_{\rm compact}/\rho$、
真实极化 $N_1$ 及上一节的 $\mathcal N_V$。
这些全部是在同一个 $z$ 上至多二次的原必要式。

每条按 $(1,z,z^2)$ 清完整分母并返回；
仅可从公共内容删除 $A,B,Q,1-Q,P_f$ 的因子。
其余每一个权因子都保留，没有使用
$m,\Phi,u+Q-1,S,u$ 或旧 $\Delta$ 等额外单位。

固定三个原行选择：
$$
(R_{\rm true},W,O),\quad
(R_{\rm true},W,N_1),\quad
(\mathcal N_V,R_{\rm true},W).
$$
若三行是 $r_i=(r_{i0},r_{i1},r_{i2})$，用后两列的交叉子式作 $c_i$，
则源完整返回
$$
\sum_i c_ir_i=(D,0,0).
$$
所以每个非零 $D$ 都是同一个原理想中的标量必要式；
其完整因式乘回后仅删除上述坐标单位，全部其他零支与重数保留。
若 $D=0$，准确记录零组合；若最终标量为非零常数，才允许声称这一明确坐标图排空。

这是真正更正后的原输入，不是重跑旧错误模型。旧原点数、Q6、
235170 或 h=k 零面关闭不能作为本源的假设。程序不恢复那些结论，
不预称新三个标量互素，也不把泛型非零或 gcd=1 作为排空。
