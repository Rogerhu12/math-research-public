# R175：实际 CM 生成元的碰撞修正 Miller 搬运

日期：2026-11-13。**状态：已证明。** 本文完整证明相交支撑上的实际纤维运输，给出层41两个CM点的准确参数单位、交换符号和规范截面接口；两条CM主函数的完整数值与第二变量高度另行续算。本文沿用R148、R154的同一范数方向，不把首系数冒充普通点值。

## 1. 相交纤维的明确生成元

设 $X/k$ 光滑射影，$k/\mathbb Q_{47}$ 有限，$P,b\in X(k)$ 不同，
$$A=P-b,\qquad D=\sum_Qd_QQ,\qquad \deg D=0.$$
在 $P,b$ 分别固定参数 $t_P,t_b$。在其余闭点只在需要时固定参数；对闭点求值始终取 $k(Q)/k$ 范数。

使用 $\mathcal P_{[A],[D]}=\operatorname{Norm}_A\mathcal O(D)$。若 $D$ 在 $P,b$ 的系数分别为 $d_P,d_b$，则
$$e_{\mathbf t}(A,D)=t_P^{-d_P}|_P\otimes(t_b^{-d_b}|_b)^{-1}$$
是这个范数纤维的明确非零元素。符号 $t^{-d}|_P$ 指线丛 $\mathcal O(D)$ 的局部生成元之纤维，不是函数 $t^{-d}$ 在点处的非法数值。

令 $A_Y$ 为与 $D$ 支撑不交的度零除子，给定实际函数
$$\operatorname{div}f=mA-A_Y.\tag{1.1}$$
在 $P,b$ 处以指定参数取首系数，在其余 $D$ 支撑上取普通非零值，定义
$$f[D]_{\mathbf t}=\prod_Q\operatorname N_{k(Q)/k}\!\left(\operatorname{lc}_{t_Q}f\right)^{d_Q}.\tag{1.2}$$
这里 $P,b$ 的阶准确为 $m,-m$；若 $d_Q\ne0$ 且 $Q\ne P,b$，由 (1.1) 和不交假设知 $f$ 在 $Q$ 无零极。所以 (1.2) 没有未定义项。

## 2. 完整碰撞搬运公式

**命题。** 在上述实际双扩张群律和范数规范下，
$$[m]_1 e_{\mathbf t}(A,D)
=(-1)^{m(d_P-d_b)}f[D]_{\mathbf t}\,e(A_Y,D).\tag{2.1}$$
特别，对固定分支的47进双扩张对数，
$$\boxed{m\lambda(e_{\mathbf t}(A,D))
=\lambda(e(A_Y,D))+\log_{47}f[D]_{\mathbf t}.}\tag{2.2}$$

**证明。** 由曲线上的弱逼近，选实际有理函数 $g$，使
$$D'=D+\operatorname{div}g$$
避开 $A$ 和 $A_Y$，且 $g$ 在 $A_Y$ 支撑均为单位。在 $P,b$ 处令
$$g=t_P^{-d_P}u_P,\qquad g=t_b^{-d_b}u_b,\qquad u_P(P)u_b(b)\ne0,$$
置 $G=u_P(P)/u_b(b)$。

乘以 $g$ 的线丛同构 $\mathcal O(D')\longrightarrow\mathcal O(D)$ 在范数纤维中给
$$e(A,D')\longmapsto G\,e_{\mathbf t}(A,D),$$
$$e(A_Y,D')\longmapsto g(A_Y)e(A_Y,D).$$
此处第一式使用实际局部生成元 $t^{-d}$，所以 $G$ 是单位部分，不是 $g(P)/g(b)$ 的非法表达式。

对不交的 $D'$ 使用R154的主函数搬运：
$$[m]_1e(A,D')=f(D')e(A_Y,D').$$
因此把两边送回 $D$ 后得到
$$[m]_1 e_{\mathbf t}(A,D)
=\frac{f(D')g(A_Y)}{G^m}\,e(A_Y,D).\tag{2.3}$$

现在用完整 tame symbol 的 Weil 互反律。以同一局部参数记 $v_Q(f),v_Q(g)$ 和相应首系数，则
$$\prod_Q\operatorname N_{k(Q)/k}
\left((-1)^{v_Q(f)v_Q(g)}
\frac{\operatorname{lc}f^{v_Q(g)}}{\operatorname{lc}g^{v_Q(f)}}\right)=1.$$
由于 $g$ 在 $A_Y$ 上为单位，而 $v_P(g)=-d_P,v_b(g)=-d_b$，符号指数为
$$\sum_Q[k(Q):k]v_Q(f)v_Q(g)=-m(d_P-d_b).$$
同时
$$g[\operatorname{div}f]=G^m/g(A_Y).$$
对每个闭点将 $d_Q+v_Q(g)$ 相加；在 $P,b$ 上两项相消，在 $A_Y$ 上两项都为零。因此
$$f(D')=f[D]_{\mathbf t}\,f[\operatorname{div}g]
=(-1)^{m(d_P-d_b)}f[D]_{\mathbf t}\frac{G^m}{g(A_Y)}.$$
代回 (2.3) 即得 (2.1)。47进对数杀掉 $-1$，给 (2.2)。这里使用 $g$ 只是证明两种真实纤维识别相等；最后表达式不含 $g$，故数值实施无须另造或另存一个大次数移动函数。证毕。

乘 $f$ 以常数不改变 (1.2)，因为 $\deg D=0$。这仅消除主函数常数自由度，不改变 $e_{\mathbf t}$ 的参数规范。

## 3. 实际CM12与CM7的适用形式

R148中 $F_2=27T_2+4$ 的第二除子为
$$D_u=27(T_2u+3u-Q_2)+4(u+b+K_{g_1}),$$
$$D_c=27(T_2c+3u-Q_2)+4(c+b+K_{g_1}).$$
这里 $u=P_{-12},c=P_{-7}$；R155及实际CM邻居数据给 $Q_2=2c+Z_{-8}$、$T_2u=b+C_{-48,+}+C_{-48,-}$、$T_2c=2c+C_{-28}$。

$D_u$ 在 $u,b$ 的系数为85和31；$D_c$ 在 $c,b$ 的系数为4和4。两者相交系数差分别为54和0，所以 (2.1) 的符号均为1；此外当前 $m=\#J(\mathbb F_{47})$ 本身也是偶数。

两条真实CM链初始除子为
$$A_{\rm initial}=P-b+\operatorname{div}h,\qquad h=f_b/f_0.$$
完整终态换框后必须使用
$$f_C=F_{\rm chain}/(g_{\rm tr}h^m),\qquad
\operatorname{div}f_C=m(P-b)-A_{mC}.$$
不能直接把 $F_{\rm chain}$ 的首单位代入 (2.2)。程序 `p41_cm_miller_prepared47.py` 保留全部初始、负点、旧终态与新终态的整盘首一因子，所得单位才是 $f_C$ 的首系数。

`2026-11-12-qc-cm-j-parameter-and-collision-units.md` 已完整核对
$$t_P=\alpha_P(j-j(P))+O((j-j(P))^2),$$
$$\alpha_b=1823234,\quad\alpha_u=3373029,\quad\alpha_c=3234143\pmod{47^4}.$$
由 $\operatorname{lc}_j f=\alpha_P^{v_P(f)}\operatorname{lc}_{t_P}f$，
$$f_{C12}[D_u]_j=1231333\,f_{C12}[D_u]_{\mathbf t},$$
$$f_{C7}[D_c]_j=852723\,f_{C7}[D_c]_{\mathbf t}.$$
对应对数增量为4804857、3347904模 $47^4$。这些式子现在是 (2.1) 中完整广义范数的参数变化，仍不把相交函数值拆成普通零除法。

R151改变到 $K_{g_1}$ 后的实际全局截面坐标为
$$\sigma_{F_2,b}(u)=698837\,e_j(A_u,D_u),\qquad
\sigma_{F_2,b}(c)=3999200\,e_j(A_c,D_c).$$
所以严格计算接口为
$$\boxed{m\lambda(\sigma_{F_2,b}(P))
=m\log_{47}s_P+\lambda(e(A_{mC},D_P))+
\log_{47}f_C[D_P]_j,}\tag{3.1}$$
其中 $s_u=698837,s_c=3999200$。右边的 $\lambda(e(A_{mC},D_P))$ 仍是实际非形式第二变量的纤维值；本命题没有把它设为零，也没有用相同Lie坐标代替其真实对应/主函数运输。

## 4. 真正不交的形式终点和精度

R167 的 $mC12,mC7$ 都采用 R141 的同一第一 Abel 族：固定72次部分与54个移动点的剩余支撑与 R151 已验的第一族 $mB$ 完全相同。移动参数全部属于 $47R$。R160/R151 已逐一证明该族的有效支撑及其固定基除子避开26个CM盘、四个典范剩余点及高102次典范因子。这些单位条件只由约化决定，所以同样给出本篇 $A_{mC}$ 与 $D_u,D_c$ 的整不交性。不能把这个事实替换为只有 Jacobian 点类相等。

完整函数 $f_C$ 仍须由正在运行的CM链及实际旧/新终点主函数取得；本篇没有预先赋予它一个数值。取得该函数以后，R159的整盘算法准确消去全部中间首一因子，只对单位求逆；各首单位均保留模 $47^4$。本篇参数因子也都是47进单位，故乘幂和 (2.1) 不损失精度。由于 $m\equiv9\pmod{47}$，(2.2) 或 (3.1) 中的除以 $m$ 也不损失精度。

这里的 $\lambda(e(A_{mC},D_P))$ 不是R145的形式对形式值：其第二变量仍是完整实际除子 $D_P$。后续可把共同平移及真实 $T_2$ 对应的函数另外搬运进入同一形式框架；仅有其Hecke坐标、相同对数或同维理想均不足以将此项删除。

## 5. 实际数值证书和依赖

参数比较由 `scripts/p41_cm_j_parameter47.py` 完成，逐项核对同一真实73维模形式的一阶展开，所有输入哈希均保存。最终小证书 `scripts/data/p41_cm_j_parameter47_certificate.json` 的SHA256为
`c6d77aad2320db6b13922e3d110348ffc0bd501495392ecbfa45ce5a3ccff06f`。

三个 $dt/dj$ 值和两个巨大指数单位因子均已实际计算；并以47进对数线性式另核最终乘幂。源可以仅用Python标准库重建：

~~~
python -B scripts/p41_cm_j_parameter47.py --script-dir scripts
~~~

本证明使用的来源和确切接口如下：

- R148，§§1、5.1及CM7附节：实际范数约定、两个 $j$ 参数生成元、完整 $D_P$ 及规范截面坐标；
- R154，§§1–2：同一方向的主除子识别；本文进一步用完整 tame symbol 给出有碰撞时的准确符号，而不是套用原先只适用于不交支撑的点值公式；
- R155：$Q_2$ 的全部真实支撑及长度；R160：整盘参数和有限代数；
- R151：改换到实际 $K_{g_1}$ 后的两个截面坐标、全部固定支撑及端点单位；
- R167：同一Abel族的实际CM形式终点和坐标规范。

所有新增运输、首系数和符号公式已在正文直接证明；不调用未发表算法或推测的高度规范。
