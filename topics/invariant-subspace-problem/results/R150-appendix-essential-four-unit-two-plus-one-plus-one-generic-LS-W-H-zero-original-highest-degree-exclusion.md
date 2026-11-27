# R150：W=0 补图 H=0 整条权曲线的原最高次系统排除

日期：2026-11-27。会话：Astra-ISP-8542378f-20261127；AI-assisted GPT-6 Astra Pro。

**已证明；严格范围。** 在一般 LS、原 Delta=0、W=0 的已付补图上，H=4ek-k^2-4k-8=0 时，原三条 mean 和 N1 关于 Gram 变量的齐次最高次部分没有非零共同根。本条覆盖这条权曲线的整个参数域及全部复嵌入。它只排除这个最高次系统的射影零点，**没有排除 H=0 的全部有限原解，也没有支付把 H 本身作为原物理单位**。前两条六次 x 必要式中已有的 H 因子仍必须保留。

## 1. 有理权曲线和全部已付参数因子

沿原 W=0 坐标
$$
e=u-1,\quad k=Q/e,\quad V=(e+1)k+2,\qquad
\ell=\frac{(e+1)((k+2)^2-2ek)}{kV},
$$
H=0 精确给出
$$
w=k,\quad A_w=w^2+4w+8,\quad B_w=w^2+8w+8,
$$
$$
e=\frac{A_w}{4w},\quad u=\frac{B_w}{4w},\quad
Q=\frac{A_w}{4},\quad \ell=\frac{B_w}{2w(w+4)},\quad
V=\frac{(w+4)^2}{4}.
\tag{1}
$$
进一步有
$$
1-Q=-\frac{(w+2)^2}{4},\qquad
bc=\frac{\ell^2}{2}=\frac{B_w^2}{8w^2(w+4)^2},
$$
$$
P02=\frac{A_w^2B_w(w+2)}{16w^3(w+4)},\qquad
\Phi=-\frac{A_w^2}{2w^2(w+4)}.
\tag{2}
$$
源码逐项回乘这些原权身份。由原 u、u−1、Q、1−Q、bc、P02 和已闭 W 首项零面，w、A_w、B_w、w+2、w+4 均为单位；当前补图还已支付 k+1=w+1。没有倒置新的权因子。

在整个常数域 QQ(i)、i^2=−1 中取
$$
r=-\frac{i(w+2)}2,\quad p=1+r,\quad q=1-r,\quad
b=\frac{\ell(1+i)}2,\quad c=\frac{\ell(1-i)}2,\quad a=1-\ell.
\tag{3}
$$
实际核验 p+q=2、pq=Q、b+c=ell、bp+cq=u、bc=ell^2/2。另一个复嵌入同时交换符号，以下所有代数身份在该嵌入仍成立；未只选一条复根进行测试。

## 2. 原最高次式的完整分支覆盖

把原 singleton Gram 的两个均值写作 X、Y，并保留原 Gram 参数 t。令共同尺度为 kappa，固定权参数，把 X、Y、t 同时乘 kappa。原 E0 先确定
$$
2f_h=F=\frac{bpX+cqY}{u}
$$
为 f 的最高次项；原 N0、P1 随后恢复同一个 lambda、T。所有恢复分母由原单位支付。

由原 mean 定义直接展开，两个 singleton mean 的最高次二次式为
$$
\frac{E_B^h}{c}=\frac{2q}{u}X(Y-X)+t(t-2Y),
$$
$$
\frac{E_C^h}{b}=\frac{2p}{u}Y(X-Y)+t(t-2X).
\tag{4}
$$
故它们的差准确等于
$$
2(Y-X)\left(\frac{qX+pY}{u}-t\right).
\tag{5}
$$
原 E1 的最高次式是
$$
E_1^h=
-2bX^2-2cY^2+2bc\,t(X+Y)+2F(F-bX-cY).
\tag{6}
$$
下面分别处理 (5) 的两支，没有倒置 Y−X 后漏掉零支。

### 2.1 X=Y 支

若 X=Y=0，则 (4) 迫使 t=0，不是射影点。否则用共同尺度令 X=Y=1；(4) 给 t=0 或2。

由 (6) 及 (1)—(2)，这两点的原 E1 最高次返回分别为
$$
2(1-2\ell)=-\frac{8(w+2)}{w(w+4)},
$$
$$
2(1-2\ell+4bc)=\frac{A_w^2}{w^2(w+4)^2}.
\tag{7}
$$
两者均是已付单位。源码另外直接从完整原 Gram 的 mean1 取 kappa^2 系数，与 (7) 逐项相等，不只核简化公式。

### 2.2 Y≠X 支及 X=0 的保留

由 (5)，
$$
t=(qX+pY)/u.
$$
两个原 singleton mean 此时均返回
$$
C(X,Y)/u^2,\qquad
C(X,Y)=q(q-2u)X^2+2pqXY+p(p-2u)Y^2.
\tag{8}
$$
在整条 H=0 曲线上，
$$
bp(p-2u)=cq(q-2u),
$$
从而原 E1 返回为
$$
E_1^h=2bc\,C(X,Y)/u^2.
\tag{9}
$$
源码核 (8)—(9) 的原多项式恒等式。

若 X=0，(8) 迫使 p(p−2u)Y^2=0。这里 p(p−2u) 是单位：由
$$
p=\frac{2-i(w+2)}2,\qquad
p-2u=-\frac{(w+2)(w+4+iw)}{2w},
$$
$$
[2-i(w+2)][2+i(w+2)]=A_w,
$$
$$
(w+4+iw)(w+4-iw)=2A_w,
$$
及已付 w、w+2、A_w 即可。源码还构造其实际逆并核所有分母只含已付因子。于是 X=0 支无射影点。

所以此支可以合法令 X=1、Y=z，保留同一个 z，并写
$$
t_*=(q+pz)/u,\quad F=(bp+cqz)/u,\quad Z=b+cz,
$$
$$
C(z)=q(q-2u)+2pqz+p(p-2u)z^2.
\tag{10}
$$

## 3. 同一个原 N1 的最高次二次式

仍用
$$
V_2=2u-\ell Q,\quad T_0=V_2-2u^2,\quad
P02=(2-3u)V_2-Qu+2u^3,\quad J=2u(1-u)+\ell Q.
$$
同一个原 N0、P1 给
$$
\Lambda=P02\,\lambda_h=
\frac{JF-2QZ+2bcQt_*}{2},
$$
$$
\Omega=P02\,(\lambda-T)_h
=\ell QF+(T_0-Q)Z+2bc(Q+2u-2)t_*.
\tag{11}
$$
设
$$
H_2=bp+cqz^2-bc\,t_*(p+qz),\qquad
H_1=uF-2bc\,t_*,
$$
$$
K_2=b+cz^2-bc\,t_*(1+z).
$$
原 N4 极化的最高次系数为
$$
\mathcal N=
4H_2-2FH_1-4uK_2
+2bc\,t_*\{p(z-bt_*)+q(1-ct_*)\}.
$$
因此原 N1 乘已付 P02 的最高次必要式恰为
$$
N(z)=P02\,\mathcal N-4\Lambda\Omega.
\tag{12}
$$
C、N 都是 z 二次式；没有让两条方程选择不同的 Gram 点或不同的 lambda。

为了支付 (11)—(12) 的原来源，自含源独立引入形式尺度 kappa，构造
$$
X_{\rm full}=\kappa,\quad Y_{\rm full}=\kappa z,\quad
t_{\rm full}=\kappa t_*,\quad
f_{\rm full}=\kappa F/2-T_0/(4u),
$$
以及完整四行原 Gram，而不是只输入上面的最高次简式。随后重新计算原 tau、双点乘法、DK、四条 mean、N4 和原 P 极化：

- 原 E0 恒为0，原 F2=2f 恒等；
- 从三条原 mean 取 kappa^2 系数，分别精确等于 (8)—(9)；
- 从原 N4(row0) 恢复完整 lambda，从原 P 极化恢复完整 lambda−1−T；它们的 kappa 系数乘 P02 后恰为 Lambda、Omega；
- 从完整原 N1 取 kappa^2 系数，再乘 P02，恰为 (12)。

原加权 Ns、Ps 的 kappa^3 系数也从完整原式独立核出；它们未被用于本条排除，因此没有以未用高次输入补强结论。

## 4. 完整 QQ(i,w) 结式和原 Bézout 单位

在上述完整原二次次数2/2上，计算4阶 Sylvester 行列式。精确结果为
$$
\operatorname{Res}_z(C,N)
=
\frac{(w+2)^2 A_w^{10}B_w^4}
{2048\,w^{10}(w+4)^8}.
\tag{13}
$$
这是 QQ(i,w) 中的精确等式，未使用有限域、数值点或多变量 gcd 判空。分子30次、分母18次；完整分子逐项除去 (w+2)^2、A_w^10、B_w^4 后恰为1/2048，所有整除及因子乘积均乘回。

源码构造4×4 Sylvester 矩阵的常数列 cofactor，实际核对全部四列，再把它返回成两个 z 一次系数多项式 a(z)、b(z)：
$$
a(z)C(z)+b(z)N(z)=\operatorname{Res}_z(C,N).
$$
(13) 是已付单位，故又实际构造其逆并完整回乘
$$
\alpha(z)C(z)+\beta(z)N(z)=1.
\tag{14}
$$
两个乘积与和均实际计算，alpha、beta 的全部分母逐项只由已付权因子构成。原 C 的 z 首项也已在2.2节支付；即使不用该首项倒置，(14) 仍是全参数局部化上的原多项式身份。

(14) 排除 (10)—(12) 的每个同 z 原共同根。加上2.1节的 X=Y 和2.2节的 X=0，原最高次系统的全部射影方向均已覆盖。

## 5. 自含源码、实际执行及准确限制

源码：[2026-11-27-unit211-generic-LS-W-H-zero-original-highest-degree-return-8542.js](../notes/2026-11-27-unit211-generic-LS-W-H-zero-original-highest-degree-return-8542.js)。

- 大小16918字节；SHA256：d39dc87cbfee0ea7f56e6bc0c44c0e49978128edb6a68d698bfdd5114e008d14。
- 完整自含 ECMAScript，仅使用 BigInt 实现 QQ(i,w) 的精确加乘、整除、Euclid 与原多项式运算，不读取缓存或外部文件。
- 实际由 functions.exec 的 V8 运行完整同一源码，正常返回；所有断言通过；源内墙钟7.287秒。
- 此执行没有创建操作系统子进程，因此 OS exit code 不适用，RSS未由API暴露。未伪造进程退出码、内存上限或RSS数值。
- 23次已付分母检查；完整原 Gram 尺度系数、4阶 cofactor、两项 Bézout 单位以及两个 X=Y 特殊方向均实际返回。
- 可再生证书对象的规范 JSON 为9356字节，SHA256：00e82fb80111239790f5e70c1fc6f0ae09b33bbdbbfc6b992efefc0c6f2290b3。
- 实际返回元数据的规范 JSON SHA256：24e04f60e4b970a66603a3c6adfd468ce33bdf33423fe8d8e4ff1f0171d9e176。
- 小回执：[2026-11-27-unit211-generic-LS-W-H-zero-original-highest-degree-execution-8542.json](../notes/2026-11-27-unit211-generic-LS-W-H-zero-original-highest-degree-execution-8542.json)。

本次执行与此前没有返回的六行三次头探针不同：新输入是 H=0 的明确有理权曲线，常数域 QQ(i)，原同 z 两个二次式的完整4阶结式；实际算术位于可用的 V8 环境。未把旧未知状态探针改标成功，也未重新启动那个未获回执的进程。

## 6. 对后续有限原解的边界

结论仅是：已付 W=0 补图中的 H=0 权曲线上，原 mean/N1 的齐次最高次系统没有非零根。因此后续这条曲线的有限代数返回可以保留这一已付的无穷远覆盖。

**H=0 的有限原系统仍须完成。** 不得由本条把原必要六次式中的 H 因子删除，不得由最高次排除推出所有有限原解为空，也不得把原 W=0 补图或课题完成状态改为已闭。
