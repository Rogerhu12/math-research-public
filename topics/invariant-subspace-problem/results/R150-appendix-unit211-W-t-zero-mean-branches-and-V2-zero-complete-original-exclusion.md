# W：t=0 的原均值两分支及整个 V2=0 纤维排除

日期：2026-11-28（Asia/Taipei）。会话 Astra-ISP-8542378f-20261127。
AI-assisted，GPT-6 Astra Pro。

## 1. 结论与原适用范围

工作在已经登记的当前一般 LS、$\Delta=0,W=0$ 物理图；原单点值互异，
所以本图原 $D\ne0$，所有既有权单位仍按各自已证范围使用。
本篇不向 $D=0$ 的辅助双数族或一般其他权图外推。

令
$$
u=e+1,\quad Q=ek,\quad V_b=uk+2,\quad
\ell=\frac{u((k+2)^2-2ek)}{kV_b},
$$
$$
V_2=2u-\ell Q,\quad T_0=V_2-2u^2,\quad
M=\ell V_2-u^2,\quad g=2\ell-1.
$$
当前整 $L_{\rm half}=0$ 排除已经给出 $g\ne0$，其中
$$
L_{\rm half}=4ke^2-(k^2+4k+8)e-(k^2+6k+8),
\qquad 2\ell-1=-L_{\rm half}/(kV_b).
$$
该单位来源是
[整 Lhalf 原排除](R150-appendix-unit211-W-entire-Lhalf-complete-original-exclusion.md)；
不把这里的 $g$ 单位用于该定理所排除的辅助原族。

本篇证明以下完整原结论：

1. 当前 W 图上，$t=0$ 的任何原解必须满足 $f=u$。
2. 当前 W 图上不存在满足 $t=0,V_2=0$ 的原解。
3. 因此 $t=0$ 的全部剩余原解都在 $f=u,V_2\ne0$ 图，且下文的
   几何参数 $w$ 由权唯一确定，满足一条明确的必要权曲线。
   本篇不宣称这条剩余权曲线已经排除。

整个 $V_2=0$ 计算只在两个二次代数里作精确运算，未选取 $z$ 或
$\rho$ 的一个根，没有对新几何首项作泛型删除。

## 2. 真正的原均值与 t=0 的两分支

原记号为
$$
p=1+\rho,\quad q=1-\rho,\quad \rho^2=1-Q,\quad
b+c=\ell,\quad bp+cq=u,\quad a=1-\ell,
$$
$$
X=x+y\rho,\quad Y=x-y\rho,\quad V=bX+cY,\quad
EW=bE_B+cE_C,\quad EBo=(E_B-E_C)/(2\rho).
$$
这里 $V$ 是几何均值，和纯权分母 $V_b$ 不同。
原 jet 乘法始终是
$$
(vw)_0=v_0w_0,\qquad (vw)_1=v_0w_1+v_1w_0.
$$
尤其原均值的平方项为 $-2(d^2)_1=-4d_0d_1$。
本篇两个新源没有调用错误 compact $E_1$ 或其后继投影。

由正确的原 $E_0$ 消元及 $E_1-EW$，在 $t=0$ 有
$$
E_1-EW=8(f-u)(f-V).
$$
这也直接是已经核实的修正紧凑式
$$
R_{\rm true}\big|_{t=0}=4Q^2(f-u)(V-f)
$$
的结果。因此全部原点落在 $f=u$ 或 $V=f$，不需要倒置这两个因子。

### 2.1 完整排除 V=f 分支

[一般 A1=t=0 的原 jet 定理](R150-appendix-unit211-original-bipartite-Gram-jets-force-value-discriminant-zero.md)已经不借 W 直接证明此支强迫 $D=0$。下面保留当前 W 中独立的显式原均值组合，作为同一闭支的另一来源，不重复计作新增分支。

令 $v=2f-u$。原 $E_0$ 与 $V=f$ 在已付 $M$ 上唯一恢复
$$
X=\frac{T_0v}{2M}+
  \left(\frac12+\frac{ugv}{2M}\right)p,\qquad
Y=\frac{T_0v}{2M}+
  \left(\frac12+\frac{ugv}{2M}\right)q.
$$
写 $h_p=(T_0+ugp)/M$，原均值逐项展开为
$$
2E_B=g\,p(p-2u)+v^2h_p(2-h_p),
$$
另一个均值只将 $p$ 换成 $q$。由
$p+q=2,pq=Q$ 及权恒等式，得到完整原组合
$$
2M\,EW=gT_0(v^2+M),
$$
$$
\boxed{MT_0EBo-2u(M-T_0-ug)EW
      =g\ell T_0R_w,}
$$
其中准确的纯权式是
$$
R_w=2u(1-u)-uQ+(2u-1)\ell Q.
$$
特别注意最后一项系数为 $2u-1$，不是 $g=2\ell-1$。
将本 W 权参数代入，直接得到
$$
R_w=-\frac{e^2uH}{V_b},\qquad
H=4ek-k^2-4k-8.
$$
这里 $\ell$ 由[一般 ell=0 完整原排除](R150-appendix-unit211-general-ell-zero-complete-original-exclusion.md)支付，
$H$ 由[整个 H_old=0 原排除](R150-appendix-essential-four-unit-two-plus-one-plus-one-generic-LS-W-H-zero-complete-original-exclusion.md)支付。
而
$
T_0=-\frac{ue(k+2)(k+4)}{V_b},\qquad M=4bc(1-Q),
$
故 $T_0,M,e,u,V_b$ 只用已登记原权单位；
$g$ 则由上述整 Lhalf 定理已付。
所以右边是单位，而左边是两个原均值的组合，矛盾。
这是整 $V=f,t=0$ 分支的原理想排除。

## 3. 剩余 f=u 分支的原几何恢复

令
$$
w=2V-(1+2\ell)u.
$$
原 $E_0$ 唯一给
$$
X=u+\frac{V_2w}{2M}
  +\left(\frac12-\frac{uw}{2M}\right)p,\qquad
Y=\overline X.
$$
亦即
$$
x=u+\frac12+\frac{(V_2-u)w}{2M},\quad
y=\frac12-\frac{uw}{2M},\quad t=0.
$$
记
$$
q_w=w^2-gM,\qquad J_0=V_2-uQ.
$$
原 $E_B$ 的完整未除首项身份是
$$
2M^2E_B+(V_2-up)^2q_w
=2M(\ell p-u)(gJ_0+V_2w).
$$
因此两条原均值给
$$
\boxed{2M\,EW=-V_2q_w,}
$$
$$
\boxed{M^2EBo-u(V_2-u)q_w=M\ell(gJ_0+V_2w).}
$$
这些是原多项式身份，尚未倒置 $V_2$。

在 $V_2\ne0$ 图，
$$
w=-gJ_0/V_2,\qquad w^2=gM,
$$
所以必要权式为
$$
\boxed{gJ_0^2-MV_2^2=0.}
$$
这里使用 $g\ne0$。每个这样的权点只有上述一个 $w$；
原 $N_1,NS,PS$ 和原个别值仍须同点返回。
这一互补图是后续新输入，不由本篇有限或数值检验替代。

## 4. V2=0 的完整权与几何模型

本 W 权参数有恒等式
$$
V_2=\frac{u(ek-2)(2e-k-2)}{V_b}.
$$
$ek=Q=2$ 整支属于[此前已排的整个等权图](R150-appendix-unit211-equal-weights-complete-original-exclusion.md)，因为
$$
(\ell-u)kV_b=u(k+2)(2-Q).
$$
故这里只剩完整权线
$$
k=2e-2,\quad e=u-1,\quad
Q=2(u-1)(u-2),\quad
\ell=\frac{u}{(u-1)(u-2)}.
$$
原权单位给 $u(u-1)(u-2)(1-Q)\ne0$，且
$$
M=-u^2,\quad T_0=-2u^2,\quad
P_{02}=2u(3u-2).
$$
所以 $3u-2$ 也已付。

在 $V_2=0$ 中，上节第二个完整均值身份变为
$$
w^2=g u^2.
$$
只倒置已付 $u$，令 $z=w/u$，得到整个首一二次代数
$$
z^2=g=2\ell-1.
$$
不倒置 $z$、不选一个平方根，也不要求这个代数为域。
几何坐标为
$$
f=u,\quad t=0,\quad
x=u+\frac{1+z}{2},\quad y=\frac{1+z}{2},
$$
$$
X=u+\frac{1+z}{2}p,\qquad Y=u+\frac{1+z}{2}q.
$$
再加入完整 $\rho^2=1-Q$，就是本次新四维系数代数。

## 5. 三个完整原 N/P 行及两个小标量组合

第一个新源从完整原四行 Gram 构建正确的 $d,DK$、原四均值、
$N_4$ 与中心化 $P_2$。
它实际返回四条均值全零，以及同一点的原 $E_0,N_0,P_0,P_1$。
特别恢复
$$
\lambda=-\frac{Q(1+z)}{4(3u-2)}
$$
和原 $T$；没有自由选择另一个 $\lambda$ 或 $T$。

令 $N_1,NS,PS$ 分别为原极化四次条件与两条原加权单点条件。
在上述整个二次代数里，它们精确等于
$$
N_1=\frac{2u^3}{3u-2}\,n(z),\qquad
NS=\frac{2u^3}{(3u-2)^2}\,s(z),\qquad
PS=\frac{2u}{(3u-2)^2}\,r(z),
$$
其中全部系数如下：
$$
n(z)=(2u^2-15u+6)-(2u^2-u+2)z,
$$
$$
s(z)=(-u^4+6u^3-11u^2+12u-4)
 +(u^4-2u^3+11u^2-12u+4)z,
$$
$$
r(z)=(-u^6+12u^5-69u^4+117u^3-98u^2+44u-8)
 +(u^6-8u^5+9u^4+37u^3-74u^2+44u-8)z.
$$
因此记 $n=n_0+n_1z,s=s_0+s_1z,r=r_0+r_1z$，
两个真正原两列 cofactor 是
$$
s_1n-n_1s=-2(3u-2)A_4,
\qquad r_1n-n_1r=-2(3u-2)B_6,
$$
$$
A_4=u^4-4u^3+23u^2-20u+4,
$$
$$
B_6=u^6+2u^5-35u^4+160u^3-200u^2+96u-16.
$$
第二个新源实际检查这两条完整 $(1,z)$ 列身份，随后得到以下整系数
Bézout 乘回：
$$
S_5A_4+T_3B_6=2208,
$$
$$
S_5=-14852u^5-39727u^4+492974u^3
      -2043739u^2+1592324u-355796,
$$
$$
T_3=14852u^3-49385u^2+308304u-89087.
$$
故
$$
(S_5s_1+T_3r_1)n-n_1(S_5s+T_3r)
=-4416(3u-2).
$$
第二个源也独立实际返回这个组合除以 2208 后的完整两列：
常数列为 $-2(3u-2)$，$z$ 列为零。
所有被除去的尺度只有已付 $u,3u-2$ 和非零有理常数，
因此这是整个 $V_2=0,f=u,t=0$ 原系统的单位组合。
没有剩余参数根，没有暂时主元零纤维，也不需要再做有限候选枚举。

合第 2 节的整 $V=f$ 排除，得到本篇第 1 节的整 $t=0,V_2=0$ 结论。

## 6. 实际执行、来源及边界

两个独立、已经执行的 V8 函数体源：

- [完整原 Gram 二次模型](../notes/2026-11-28-unit211-W-t-zero-V2-zero-full-original-quadratic-return-8542.js)，
  10171 字节，SHA256
  51f361d924a306f2df1b1ea969688ad527b89ab4baa2650b1c3da9a4736d0658。
  实际 0.565 秒；1161286 次有理数运算、106700 次多项式运算，
  15488 次精确除法/乘回计数；全部原返回通过。
- [原两列组合及完整 QQ Bézout](../notes/2026-11-28-unit211-W-t-zero-V2-zero-original-two-column-QQ-Bezout-8542.js)，
  4179 字节，SHA256
  4e437b6efef677251d9be190dc779a1b3bbeed4053802fda41462aec1c2008ed。
  实际 0.001 秒；两原 cofactor、显示的整系数 Bézout 和最终完整两列乘回全部通过。

这些文件是实际 Function(source)() 执行的完整函数体，而不是
未运行的 Node 包装程序。第一个返回对象的 output 是数学小回执，
internals 仅供同一函数调用内扩展；无需保存它或重放旧大门。
第二个直接返回小回执。另从第一次既有原行返回对象逐系数确认 §5 的三条缩放式：六个 $(1,z)$ 系数交叉相乘差均为零，未重新执行 Gram。该小确认并入下列回执。这里不是 GitHub Actions 运行，
没有虚构 job、RSS 或进程退出码。

[小回执](../notes/2026-11-28-unit211-W-t-zero-V2-zero-complete-original-receipt-8542.json)
保存实际身份、参数定义和 SHA，不保存可重算矩阵或大系数载荷。

第 2、3 节的通用原均值身份是纸面逐项展开，不冒充本次
专门化执行的额外检验；其原乘法和均值定义与第一个源一致。
错误 compact E1 链不被引用。旧七行 Popov、旧六阶范数、
全权 determinant、已成 Lhalf/F101 门均未重新执行。

本篇关闭的是整个 $t=0,V_2=0$ 原支，并把全部剩余 $t=0$ 原解
准确送入第 3 节唯一恢复的权曲线。整个 W 尚未由本篇排除，
一般 ISP 完成标准也尚未达到。
