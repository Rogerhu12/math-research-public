# 新输入：最后一个 P201 块的完整原 Gram 值，保二次重根的 20 维整模型

日期：2026-11-28（Asia/Taipei）  
状态：首次执行前的新原输入；不预告单位返回。

## 1. 同一来源与本次范围

范围仍是 unit211、$\Phi=0$、物理 $D\ne0$ 的 H1 余图。前一来源已经在第五个完成块支付同一个 $Q,\lambda$，原 $1,T,v$ 列商的 $K_\phi$ 维数为 $1$，其中 $\deg\phi=5$。本次从原剩余 O 列与交换子 T 列的全部 $u^a$ 倍，取最后两个几何坐标对应的 $10$ 行，核完整原方阵乘逆，再放回全部 $15$ 行，准确返回
$$
u^a(T-\overline T),\qquad
u^a(v-\overline v),\qquad0\le a<5.
$$
全部原来源节点和两个真乘法矩阵在同一个 $(\overline T,\overline v)$ 上返回。

这只识别实际完成整商的剩余坐标，不认定有理 T、v 因子。实际原几何商记为 $C_\phi$，它是 $O_\phi$ 的某个有限商；不要求无挠、平坦或等于 $O_\phi$。

根会话的新 F9 原 Dixon 专门化已经完整返回 rank 0、$wD_8=0$、$w e_0=1$，并用实际 h 的整 Bézout 与完整模因子模式关闭前四块。因此当前只余第五块，旧原界是 $5$ 个权对、$5$ 个三元组、$5$ 个五坐标、$10$ 个完整规范点。本源不重算 F9，也不改写此前 167/334 的真实历史返回。

## 2. 不倒物理 D 的完整值二次

沿用
$$
\ell=1-\frac{2(u-1)(u-2)}Q,\quad
m=u-\ell,\quad \delta=1-Q,
$$
$$
A_2=2\lambda^2-2\lambda+1,\qquad
B_3=4\lambda^3-6\lambda^2+3\lambda-1.
$$
先在整个实际剩余商核 Q、$\delta$、$\ell$、$P_f$、$bc$ 的原单位，而不把原特征零非零自动当成模单位。任何必需单位未返回，整块保留且不换素数。

加入首一二次
$$
\rho^2=\delta
$$
后，取
$$
b=\frac{\ell+m/\rho}{2},\qquad
c=\frac{\ell-m/\rho}{2}.
$$
源核 $b+c=\ell$、$(b-c)\rho=m$、$bc=M/(4\delta)$。只用已实际返回的 $\delta$ 和 $bc$ 单位得到整个二次代数中的 $\rho,b,c$ 真逆，不选择一个平方根。

令 $x=h_B-1$，$y=h_C-1$。原一矩与二矩是
$$
bx+cy=T,\qquad bx^2+cy^2=A_2.
$$
因此使用
$$
y=(T-bx)/c,
$$
以及真正首一的二次式
$$
x^2-\frac{2T}{\ell}x+\frac{T^2-cA_2}{b\ell}=0. \tag{2.1}
$$
它在 $D=\ell A_2-T^2=0$ 时仍保留整个重根与幂零部分。本源没有倒置 D、矩判别式、$h_B-h_C$ 或 m。再加入真实三矩
$$
bx^3+cy^3-B_3=0.
$$

得到的实际整环境是 $C_\phi$ 上两个首一二次构成的有限代数，至多有 $4$ 个生成元。故其 $1009$ 进基环生成数至多 $20$；即使 $C_\phi$ 有挠，有限模 Nakayama 仍可使用。

## 3. 同一点恢复完整原 Gram

原 $v$、$z$ 的关系及两均值为
$$
z=\frac{v-Jf+G}{bc},\quad t=z/Q,\quad
bX+cY=v/Q,\quad bpX+cqY=(T_0+4uf)/2,
$$
其中 $p=1+\rho,q=1-\rho$、$f=-P_c/P_f$。由已付原权单位恢复
$$
X=\frac{W-qV}{b(p-q)},\qquad
Y=\frac{pV-W}{c(p-q)},
$$
$$
r=X-(1-\ell)p-ct,\quad
s=Y-(1-\ell)q-bt,\quad
A_1=2f-2bX-2cY+2bc\,t.
$$
这里 $V=v/Q$、$W=(T_0+4uf)/2$，与值向量使用不同记号。

整个原四维代数的 Gram 行为
$$
(0,0,p,q),\quad(0,A_1,r,s),\quad(p,r,0,t),\quad(q,s,t,0).
$$
采用 [已刊 U-value atlas](../results/R150-appendix-essential-four-unit-two-plus-one-plus-one-original-U-value-atlas.md) 的真实双点乘法
$$
(vw)_0=v_0w_0,\quad
(vw)_1=v_0w_1+v_1w_0,
$$
简单点逐点相乘，且
$$
\tau(v)=(1-\ell)v_0+v_1+bv_B+cv_C.
$$
第一双点的第二坐标保持为 germ，没有误作一个简单点。

本源直接形成全部四均值、P1/N1、NB/NC/PB/PC、三矩，以及值向量
$$
\mathcal V=(1,\lambda-1-T,1+x,1+y)
$$
的完整 $N_4(\mathcal V)$。归一沿原定义
$$
N_4=4N,\qquad P_2=2P,
$$
所以个别原式准确是
$$
N_4(\mathrm{row}_B)-2\lambda P_{02}h_B^2,\qquad
P_2(\mathrm{row}_B)-P_{02}h_B^3
$$
及 C 版本。所有式保同一个权点、同一个 $\lambda,T,v,\rho,x$，没有先取范数或换原值来源。

## 4. 完整原理想与准确收尾

将全部原式乘整个 $u^a\rho^i x^j$ 基，$0\le a<5$、$0\le i,j<2$，得到真实 $20$ 行理想矩阵。若满秩，选原列方阵并完整核方阵乘逆与常数 $1$ 的原组合。有限整原商的 Nakayama 引理才排除整个第五完成块。

若未满秩或任何所需原权不是整单位，则记录真实余维、缺失单位和全部未闭范围；不以模 D 为零排块，不改素数，不宣称一般图已空。只有第五块也得到完整原单位，合已经关闭的 F9 四块，才排除当前 H1 余图。普通不变子空间问题仍另有未闭接口。

## 5. 来源和资源

唯一新源：
2026-11-28-unit211-Phi-zero-H1-P201-last-block-complete-original-Gram-values-8542.py。

直接新增依赖：
2026-11-28-unit211-Phi-zero-H1-P201-fifth-block-actual-lambda-and-original-Tv-8542.py；
环境变量 ISP_H1_P201_FIFTH_GEOMETRY_SOURCE；SHA256
15a58c3d848d866e5feaf89a6a5cd939c265b8fe3c1a3f6788a2252c163ffa5b。

再沿其准确七文件链，合计八个依赖文件。原 Gram 的短普遍定义直接按已刊 atlas 写入，不执行旧 SymPy atlas 检查；其旧源身份是 blob 91fad0d4be319fe57760ac51f7ee2a6b448bbb5a、SHA256 da790bddccce690e0e12cbe3941b6c02c2912319f646c5195834408b4bde965f。

固定 $120$ 秒、$1$ GiB。依赖中的历史 JSON 仅在 runner 临时目录恢复；不经工具搬运系数载荷，也不重放旧独立结果驱动。只用必要前缀恢复本次原点和完整值的新目标。
