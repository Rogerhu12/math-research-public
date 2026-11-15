# R699 — 原首边界的统一两位判据与有限真实来源窗口

日期：2026-11-15。**状态：已证明。** 主目标仍未完成。

R700 的对数高度界使原首边界的准确零判定，从无限尾等式降为
一个统一的两位条件。本文明确给出这些条件、最后一行少一位的
精确形式，以及从同一个原 sigma/整坐标恢复它们所需的有限 jet。
这里不把“两位”解释为只有两条标量行；总计仍有 \(2p-3\)
个剩余域位，原中央到这些行的联系尚未付清。

## 1. 原对象及固定阈值

始终保
$$
p=6s-1>101,\quad q=p^2,\quad d=p+1,\quad e=p-1,
\quad K_p=\mathbf Q_p(\omega),\quad\mathcal O=\mathcal O_{K_p}.
$$
R663 的同一严格 LT 坐标、首边界与完整来源为
$$
[-p](v)=-pv+v^q,\quad W=v^d,\quad Q(W)=W^e-p,
$$
$$
\Phi_m(u(v))=v^{d-m}\mathcal B_m(W),\quad
\mathcal B_m(W)=\sum_{n\ge0}b_{m,n}W^n\in\mathcal O[[W]],
\quad m=34,72.
\tag{1}
$$
所有 \(b_{m,n}\) 都是原规范的准确系数，不是任选模 \(p\) 提升。

R696/R700 已在共同域 \(W_{\rm abs}\subset K_0(E[p^2])\) 中定义原迹
$$
\mathcal T_{m,T}=\operatorname{Tr}_{W_{\rm abs}/E_W}
     (w_T^{-m}\phi_m(T)),\qquad w_T^p=a_T.
$$
用 \(W_{\rm abs}\) 区别数域和 (1) 的形式变量。
对原非零 \(p\) 挠点 \(T\)，置 \(\xi=v_T^d\)，则
$$
\xi^e=p,\qquad
v_p(\mathcal T_{m,T})=\frac1e+v_p(\mathcal B_m(\xi)).
\tag{2}
$$
零时两边同时为无穷。全部相位、原 \(G_T\) 与全 \(H\) 项均按 R696
保持，(2) 不另选相对根。

R700 的固定常数为
$$
D_m=7\,2^{\lceil m/3\rceil}3^{\lceil m/4\rceil}17^{\lceil m/6\rceil},
\qquad C_m\ge1,
$$
其中 \(C_m\) 是原紧复环面上
\(|\mathfrak k(z)|^m|\phi_m(P(z))|\) 的固定上界。
准确已有
$$
D_m\mathcal T_{m,T}\in\mathcal O_{E_W},\qquad
|\iota(D_m\mathcal T_{m,T})|\le(p+1)D_mC_m
\tag{3}
$$
对所有绝对嵌入同时成立；\(E_W\) 只有一个 \(p\) 位。

以后取任一固定阈值 \(p_0\)，使对两个 m 和所有 \(p>p_0\)，
$$
\boxed{p^2>(p+1)D_mC_m.}
\tag{4}
$$
例如令 \(p_0>\max(101,2D_{34}C_{34},2D_{72}C_{72})\) 即可。
这是只依两个固定原来源的阈值，没有随 p 选择常数。

## 2. 准确迹零当且仅当属于 p²

**引理 1。** 对 \(p>p_0\) 和任一原 \(T\ne0\)，
$$
\boxed{\mathcal T_{m,T}=0
\iff v_p(\mathcal T_{m,T})\ge2.}
\tag{5}
$$

证明：反向的唯一问题是非零迹。若它非零，R700 的唯一 \(p\) 位高度式给
$$
v_p(\mathcal T_{m,T})\log p
\le\log((p+1)D_mC_m)<2\log p,
$$
与右边矛盾。

也可完全用整数范数重写。令 \(n=[E_W:\mathbf Q]\)、
\(\alpha=D_m\mathcal T_{m,T}\)。唯一 \(p\) 位使
$$
v_p(N_{E_W/\mathbf Q}\alpha)=n\,v_p(\alpha).
$$
若 \(v_p(\alpha)\ge2\)，其非零整数范数绝对值至少 \(p^{2n}\)；
(3) 却给严格小于 \(p^{2n}\)。这同时说明次数为何准确消掉。
\(D_m\) 为 \(p\) 单位，所以不改变 (5)。证毕。

这个结论判定的是原全迹的准确零，不是“足够小就近似为零”。

## 3. 全部无限尾变成两个原系数块

R663 的完整整 Weierstrass 余数为
$$
R_m(W)=\sum_{i=0}^{e-1}r_{m,i}W^i,\qquad
r_{m,i}=\sum_{k\ge0}p^k b_{m,i+ek}\in\mathcal O.
\tag{6}
$$
因此
$$
\mathcal B_m(\xi)=\sum_{i=0}^{e-1}r_{m,i}\xi^i.
$$
因为 \(K_p\) 未分歧，每个非零 \(r_{m,i}\) 的赋值为整数。
不同 i 的项赋值模 \(\mathbf Z\) 为不同的 \(i/e\)，不能在最低赋值处
互相抵消。所以只要不是全部为零，
$$
\boxed{
v_p(\mathcal B_m(\xi))
=\min_{0\le i<e}\left(v_p(r_{m,i})+\frac{i}{e}\right).
}
\tag{7}
$$
这使用整个 Eisenstein 剩余环，不假定某个系数预先为单位。

结合 (2)、(7)，准确有
$$
v_p(\mathcal T_{m,T})\ge2
\iff
\begin{cases}
r_{m,i}\in p^2\mathcal O,&0\le i\le e-2,\\
r_{m,e-1}\in p\mathcal O.&
\end{cases}
\tag{8}
$$
最后一行只需一位，是因为 (2) 的 \(1/e\) 加上 \((e-1)/e\)
恰为一；该原因子不可删除。

(6) 的 \(k\ge2\) 部分整体属于 \(p^2\mathcal O\)，而最后一行的
\(k\ge1\) 部分属于 \(p\mathcal O\)。故 (8) 等价于有限条件
$$
\boxed{
\begin{aligned}
b_{m,i}+p\,b_{m,i+e}&\equiv0\pmod{p^2},
&&0\le i\le e-2,\\
b_{m,e-1}&\equiv0\pmod p.&
\end{aligned}}
\tag{9}
$$
这不是截断无限尾以后假设它为零；尾的全部贡献已按所需模数支付。

## 4. 原首边界与同 Y 闭盘的有限充要判据

**定理。** 对两个原 m、所有 \(p>p_0\)，以下条件等价：

1. (9) 的全部原有限同余成立；
2. \(\mathcal T_{m,T}=0\) 对一个非零 \(p\) 挠点成立；
3. \(\mathcal B_m(\xi)=0\) 对一个根 \(\xi^e=p\) 成立；
4. \(Q\mid\mathcal B_m\) 于 \(\mathcal O[[W]]\)；
5. R663 的同一个
   \(Y_m=H^{-m}\mathcal R_m(WH^d)\) 属于闭首边界 Tate 代数，
   并延到略大的盘。

证明：1 与 (8) 等价，再由引理1得到2；2与3由原 (2) 及其完整乘法
身份等价。因 (6) 的余数次数小于 e，而 \(Q=W^e-p\) 在 \(K_p\)
上 Eisenstein、不可约，3使整余数全零，故3与4等价。
这里也可使用 R696 的全 G 传播；不将其它轨道丢掉。
4与5正是 R663 已付的同一原连接、严格常数主导及全盘粘合定理。
反向依同样的等式成立。证毕。

特别，(9) 中任一条失败，就严格证明原首边界非零、原 \(Y_m\)
不属于该闭盘；无需求任意高 \(p\) 进精度。

充分但稍冗余的版本是对所有 \(0\le i<e\) 都要求
\(b_{m,i}+p b_{m,i+e}\equiv0\bmod p^2\)。
(9) 保留了最后一行真正少一位的成本。

全部条件共涉及 \(e-1\) 个模 \(p^2\) 同余和一个模 p 同余，
即 \(2e-1=2p-3\) 个剩余域位。
“统一两位判据”并不把这些真实行压成原两个中央标量。

## 5. 所需真实 sigma 与整坐标窗口

这里给出从原来源恢复 (9) 的有限过程，并明确其 p 依赖成本。
不用任何已删除的数据文件，也不从新自由来源定义系数。

写同一个原
$$
u=x^{-1/2},\qquad u(v)=vV(v),\quad V(v)\in1+v\mathcal O[[v]],
$$
$$
\phi_m(P(u))=u^{-(m-6)}P_m(bu^6),
$$
其中
$$
\begin{aligned}
P_{34}(t)&=(1+t)(1-8t)(7-4t+16t^2)/7,\\
P_{72}(t)&=P_{34}(t)(1+4t)
 (1-96t+48t^2+64t^3)(1+20t-8t^2).
\end{aligned}
\tag{10}
$$
这些是原全多项式而不是极项近似。

定义完整整单位乘积
$$
A_m(v)=V(v)^{-(m-6)}
 T_{\rm g}(u(v))^{-m}P_m(bu(v)^6)\in\mathcal O[[v]].
\tag{11}
$$
原 Laurent 来源为
\(F_m(u(v))=v^{6-m}A_m(v)\)。
范数一投影只保 \(m+(6-m+n)\equiv0\bmod d\) 的项，因此准确有
$$
\boxed{b_{m,j}=[v^{d-6+dj}]A_m(v).}
\tag{12}
$$
没有在投影后再丢某个 C、原多项式项或规范高尾。

(9) 所需最大指标为 \(j=2e-2\)，故定义
$$
\boxed{
L_p=d(2e-1)-6=2(p^2-1)-(p+1)-6=2p^2-p-9.
}
\tag{13}
$$
只需以下完整有限 jet：

- \(V(v)\bmod v^{L_p+1}\)，即 \(u(v)\bmod v^{L_p+2}\)；
- 原 \(T_{\rm g}(u)\bmod u^{L_p+1}\)；
- (10) 的原固定两个多项式。

据此在 (11) 中作完整截断合成并取 (12)，就得到 (9) 的所有系数。
\(L_p\) 与 m 无关，故两个原来源共用同一坐标和规范窗口。
如果只保较低窗口，则 (9) 的末端原系数通常尚未被读取，不能省略。

### 5.1 有限 jet 本身的确切来源

原
$$
z(u)=\int_0^u(1+bt^6)^{-1/2}\,dt
$$
具有有理系数。其形式逆 \(u(z)\)、原
\(\sigma(z)/z\)、以及 R639 的
$$
F(z)=\log(\sigma(z)/z),\quad
F_{\rm c}(z)=\frac1d\sum_{\zeta^d=1}F(\zeta z),\quad
T_{\rm g}(u)=\exp(F_{\rm c}(z(u))-F(z(u)))
\tag{14}
$$
均在每个有限阶由有理数运算唯一决定。
\(F_{\rm c}\) 只保 z 次数为 d 倍数的原系数；
(14) 不需要给复或 p 进指数作越界函数取值。
原 \(T_{\rm g}\) 的整性另已由 R639 的 CM 极限证明。

同样，用原形式同态
$$
f(u)=[-p]_E(u)=u(-p z(u))
$$
的有限 jet，按 R663 的递推构造
\(v=h(u)=u+\cdots\)：
若第 n 阶误差为 \(E_n\)，修正系数准确为
$$
-\frac{E_n}{(-p)^n+p}.
\tag{15}
$$
分子含 p，分母除 p 后为单位，所以得到整坐标。
正式逆给 (13) 要求的 \(u(v)\)。
所有形式合成在指定次数后截断，有限步骤即结束。

可以全程用准确有理数，最后约去实际分母后才读模 \(p^2\)。
若改用有限精度实现，则须为 (14) 的 log/exp、形式反演以及 (15)
逐项支付中间精度损；本文没有声称输入只要两个 p 进位就足够。
最终 b 系数的两位与上游计算所需精度是两件不同的事。

### 5.2 不把该窗口当免费全局来源

(13) 是 \(O(p^2)\) 阶的实际来源窗口；坐标和中央规范也依赖 p。
准确有理计算的位复杂度、这些有理数的全局高度、以及旧
\(\mathcal W_D\) 来源预算并未因此变为常数。
本篇不把它们加入原固定多项式格，或自动回到旧同 R 短矩阵。

## 6. 更一般的固定精度形式

为区别“最后一行少一位”的结构和所用全局界，任取整数 \(r\ge1\)。
由同一个 (2)、(7)，准确有
$$
v_p(\mathcal T_{m,T})\ge r
\iff
\begin{cases}
\displaystyle\sum_{k=0}^{r-1}p^k b_{m,i+ek}
 \equiv0\pmod{p^r},&0\le i\le e-2,\\[2mm]
\displaystyle\sum_{k=0}^{r-2}p^k b_{m,e-1+ek}
 \equiv0\pmod{p^{r-1}}.&
\end{cases}
\tag{16}
$$
当 \(r=1\) 时最后一行为空条件。
所需最大 b 指标为 \(re-2\)，相应来源窗口为
$$
L_{p,r}=d(re-1)-6=r(p^2-1)-(p+1)-6.
\tag{17}
$$
只要 \(p^r>(p+1)D_mC_m\)，同样由范数证明使 (16)
等价于准确迹零。R700 付的是所有充分大 p 的固定选择 \(r=2\)；
没有付 \(r=1\)，因为当前复迹界仍允许大小 \(O(p)\)。

## 7. 与原中央及高 Q 条件的准确关系

R663 的同一个原中央满足
$$
j_m=(mc)^{-1}
\left[\sum_{n\ge0}(-\mathcal D_m)^n(k\mathcal B_m)\right]_{W=0}.
\tag{18}
$$
其中 \(a-c\)、k 和全部规范尾项均保留。
本文尚未从 \(j_m=0\) 推出 (9)，也未把 (9) 称为另一个中央零。
一个标量的 (18) 不能无证明地代替 \(2p-3\) 个真实剩余域位。

即使 (9) 全部成立，它首先只付同一 Y 的闭边界。
原 \(X=WH^d\) 下降仍需
\(j_m=0\)、\(Q^{d-m}\mid\mathcal B_m\) 及原同解下降条件。
零阶迹的固定分母与紧环面界没有自动支付高 Hermite jet 的对应界。

后续接口因此已完全有限而保持原来源：
把原中央、原指定提升或同 R 真像与 (9) 的全部系数实际联立；
或者在这些同一原系数上证明足够的非退化，再接已经支付的算术桥。
无穷素数和固定曲线的主目标仍未完成。

## 依赖

- [R663](R663-original-lubin-tate-residues-and-closed-boundary-equivalence.md)：
  原严格整坐标、完整余数及同 Y 闭盘充要。
- [R696](R696-original-absolute-roots-p2-field-and-linear-height-trace.md)：
  同一个原绝对根、迹、全 G 传播及准确赋值偏移。
- [R700](R700-original-fixed-denominator-and-logarithmic-trace-height.md)：
  固定全分母、全部绝对嵌入界和唯一 p 位。
- [R639](R639-complete-original-central-gauge-and-full-formal-disc-stokes.md)：
  原完整 \(T_{\rm g}\) 和同一中央值。
- [R660](R660-original-torus-coordinate-and-boundary-resonance-ideal.md)：
  原全多项式与正规的有理系数系统。

本文为一般 p 的证明和有限算法说明；没有新增数值扫描或可重算输出。
