# R235 反射轴的三阶迹兼容性、原 M12 准确跳跃与局部 C2 补丁

状态：完整局部定理、原准确数据的有理见证及一个明确的新局部修正规则。**没有证明 metric 的正 sup 下界，没有排除 C2 等距面，没有排除简单节点逐细化的 C2 收敛。当前实际 CI 场未应用本节定义的新补丁。**

本结论不重做 [R189](R189-cardinal-cubic-and-angular-exact-nesting.md) 的不同 spline 空间嵌套判断。这里使用完整 Gram 与 Gauss 恒等式，判断**同一源的第三径向迹跳跃是否能由当前反射保留的 C3 修正消去**。

## 1. 非特征接合的第三迹引理

在一个材料环带的内圈 $r=r_0$ 附近，假设：

1. 固定正定度量 $g$ 在整邻域为 $C^3$；
2. $Y$ 是整邻域的 $C^2$ 浸入，且在两侧分别为 $C^3$，全部三阶偏导有连续的一侧边界迹；
3. $Y^*e=g$ 在两侧成立；
4. 以连续定向法向 $n$ 定义 $L=n\cdot Y_{rr}$、$M=n\cdot Y_{ru}$、$N=n\cdot Y_{uu}$，在所考察边界点 $N\ne0$。

则
$$
[Y_{rrr}]=0. \tag{1}
$$
方括号表示外侧减内侧，即增加 $r$ 方向的右迹减左迹。

### 证明

设 $A=[Y_{rrr}]$。共同的 $C^2$ 迹函数 $Y_{rr}(r_0,u)$、$Y_{ru}(r_0,u)$、$Y_{uu}(r_0,u)$ 在 $u$ 上可微：两侧到边界的 $C^3$ 假设保证其切向导数等于相应混合三阶迹。因此
$$
[Y_{rru}]=[Y_{ruu}]=[Y_{uuu}]=0. \tag{2}
$$
不能仅由“数值上两 jets 很近”推出 (2)；这里用的是准确共同函数和边界正则性。

两次微分 $Y_r\cdot Y_r=g_{rr}$，取边界跳跃，得到
$$
0=[\partial_r^2g_{rr}]
=2Y_r\cdot A.
$$
同样从 $Y_r\cdot Y_u=g_{ru}$ 得
$$
0=[\partial_r^2g_{ru}]
=Y_u\cdot A,
$$
其中其余项由共同两 jets 和 (2) 消掉。因此 $A$ 垂直于两个独立切向量，故 $A=(n\cdot A)n$。

由于 $Y\in C^2$，$n$ 和 $n_r$ 都具有共同连续迹；由 (2)，
$$
[N_r]=[M_r]=0,\qquad [L_r]=n\cdot A.
$$
Gauss 恒等式
$$
LN-M^2=K(g)\det g
$$
在两侧成立。$g\in C^3$ 使右侧为 $C^1$，因此径向微分后取跳跃得
$$
N(n\cdot A)=0.
$$
$N\ne0$ 给 $n\cdot A=0$，结合已证的切向正交即得 (1)。证毕。

## 2. 当前实际对称性为何支付 N 非零

**单独 $K<0$ 不足以推出 $N\ne0$**：若 $N=0$ 而 $M\ne0$，仍有 $LN-M^2<0$。本题当前分支还满足真实环境反射
$$
Y(r,-u)=\mathcal RY(r,u),
\qquad \mathcal R=\operatorname{diag}(1,-1,1). \tag{3}
$$
在 $u=0$，$Y_r$ 位于 $xz$ 平面，$Y_u$、$Y_{ru}$ 均沿 $y$ 轴。浸入性使 $Y_r,Y_u$ 独立，因此法向 $n$ 也位于 $xz$ 平面，故
$$
M(r,0)=n\cdot Y_{ru}=0.
$$
若此处 $K(g)<0$，Gauss 给 $LN=K\det g<0$，从而 $N\ne0$。因此第 1 节引理在该反射轴上适用。

当前准确原源的平面 Fourier 系数均为实数，其频率为 $3k+1$；高度是实余弦 $3k$。所以原源满足 (3)。当前 M12 BVP 的修正也由同类实系数组成。其实际角变量是中央 $\theta$，但 $J(\theta)=|\gamma'(\theta)|$ 为偶函数，故准确材料角升映射
$$
U_0(\theta)=\bar a^{-1}\int_0^\theta J(t)\,dt
$$
是奇函数，逆映射亦奇。因此把修正转换回真实材料 $u$ 后仍准确满足 (3)，并不是仅在网格上观察到的对称。

本结论只限制保留该反射的修正，或另行支付 $N\ne0$ 的修正；**不声称排除了任意无对称 C3/C4 修正**。

## 3. 原源 node 18551 的准确非零见证

使用已冻结原 manifest
`2026-11-09-db6f-tail-inc-flat17-m12-critical-r01-s64-q512-manifest.json`，SHA
`cc23977e25a09c34db91723dd784cab4b18b89e325fc2ca2fb8dd7ee6866a104`。
只恢复最后一个原块 `raw000-part02.f64.gz`：

- Git blob `1a9cce86c3ad6e88bc07dedb465a08066a62a5ab`；
- SHA256 `89fe80d3453aa25978c343f7d58d51a31dd1d3fe37e6fffcdd48cfc31b551249`；
- $406\times567$ 个 little-endian binary64 元素，完整包含 $141$ 个位置系数通道。

取最后一个内部原源节点 $i=18551$，相邻源 span 为 $18550,18551$。程序使用原准确有理归一化 $\beta$ 与最后保存的准确 dyadic 增量 $\ell$，定义
$$
r_0=c-\beta\ell_{18551},
\qquad
\beta\ell_{18551}=2.02975232546436\ldots\times10^{-7}.
$$
故 $r_0=0.5999997970247675\ldots$；这些小数仅显示，回执保留完整有理数。没有用显示半径之差或近似存储位置来微分。

原 $F_r$ 四次 Bernstein 控制为
$$
b_0=f_0,\quad b_1=f_0+Ls_0/4,\quad
b_2=\{16m-5(f_0+f_1)-L(s_0-s_1)\}/6,
$$
$$
b_3=f_1-Ls_1/4,\qquad b_4=f_1.
$$
因此准确两端第三径向导数为
$$
F_{rrr}(0)=\frac{12}{L^2}(b_2-2b_1+b_0),\qquad
F_{rrr}(1)=\frac{12}{L^2}(b_4-2b_3+b_2). \tag{4}
$$
对全部 $141$ 个通道分别用 (4)，再按原完整 Cartesian Fourier 定义在 $u=0$ 合成，得到
$$
A=[X_{rrr}](r_0,0)
=(-1.68678477970504\ldots,\ 0,\ -0.00771337534412019\ldots).
$$
准确有理比较实际给
$$
A_x<-\frac{42}{25},\qquad A_z<-\frac{77}{10000}; \tag{5}
$$
所以这里不是量级极小但符号未认证的浮点残量。

### 背景确实在此解析且 K<0

原 [alpha 证明](../notes/2026-11-09-db6f-tail-tight-alpha-proof.md) 及其审计已给 $\alpha>90$，原完整背景已给 $0<w\le16/15$。在原 $n=0,j=8$ 的外段，$x\in[0,1]$，$\eta$ 是原 `delta0` 与 `etaRatioAtN0` 两个准确 dyadic 参数的乘积；该段使用未封顶的 raw override，权为 $1$，且
$$
(\log w)_x=-7\eta/\sqrt{12}<0.
$$
准确径向 Jacobian 为 $A_0+\alpha B_0>0$。在 $x\in[0,1/2]$，有 $\chi=1-S(x)\ge1/2$、$r_{\rm old}\ge r_{\rm cuff}$、$\sqrt{12}<4$、$1+w^2\le481/225$，故整个 $j=8$ 段的物理宽度严格大于
$$
\frac{90r_{\rm cuff}\eta}{16(481/225)}
>0.0001184056.
$$
该段的外端准确等于 $c$，而 $c-r_0<2.030\times10^{-7}$，所以 $r_0$ 严格位于此段内部。这里 raw、封闭光滑权及径向 Jacobian 都是解析的且 Jacobian 正；因此 $w(r)$ 在 $r_0$ 邻域解析，$w_r<0$。原度量
$$
g=(1+w^2)dr^2+r^2du^2
$$
在此解析，并有
$$
K(g)=\frac{ww_r}{r(1+w^2)^2}<0. \tag{6}
$$
旋转背景本身的第三导数在该邻域连续，故 (5) 确实是完整 $X$ 的 jump，而非只截取扰动的一部分。

## 4. 对当前有限空间的准确结论

R223 的 $r(q)$ 在此邻域解析且 $r_q\ne0$。当前五次简单内部节点 B-spline 修正在单位 $z$ 中为 $C^4$，转换至 $r$ 后仍为 $C^4$。中央确定修正 $C$ 的支撑远离 $r_0$，所以它在此为零。若当前某个反射保留的有限场 $Y=X+C+W$ 恰为同 $g$ 的准确等距浸入，则 $[Y_{rrr}]=A$，但第 1–2 节与 (6) 又强制 $[Y_{rrr}]=0$，与 (5) 矛盾。

此结论不产生 $\inf\|Y^*e-g\|_\infty>0$。更细简单节点可以在更窄层中近似所需的 C2 修正；它们的三阶导数连续性不必在 C2 极限中保留。不能据此否定已启动的 source-aligned h 试验，也不能据此声称固定 $g$ 已无解。

## 5. 一个准确消跳、端口不动的 C2 修正

此节给出具体可再生输入，避免将局部兼容性结果只写成否定。令 $A(u)$ 为第 3 节计算的**完整 Fourier jump 向量**，不只取 $u=0$ 的值。设
$$
\delta=\frac{\beta\ell_{18551}}3,
\quad S_3(t)=35t^4-84t^5+70t^6-20t^7,
$$
$$
B(y)=
\begin{cases}
0,&y\le0,\\
y^3/6,&0\le y\le1,\\
y^3[1-S_3(y-1)]/6,&1\le y\le2,\\
0,&y\ge2.
\end{cases}
$$
定义另一个准确场
$$
Q(r,u)=-\delta^3 B((r-r_0)/\delta)A(u). \tag{7}
$$
因为 $S_3$ 的一、二、三阶导数在 $0,1$ 都为零，$B$ 在 $y=1,2$ 为 $C^3$，且 $B'''(0+)=1$。因此 $Q$ 为全域 $C^2$，只在 $r_0$ 有第三导跳 $-A(u)$。其支撑严格位于 $[r_0,r_0+2\delta]$，仍在最后一个原 span 内，不碰 $c$、中央或真 cuff。于是 $X+Q$ 在这个完整材料圆周的三阶迹准确接合，且 cutoff 两端没有新三阶 jump。全部原反射/D3 对称由 $A(u)$ 保留。

用两个分片的准确 Bernstein 系数，程序得
$$
\|B\|_\infty\le37/90,\quad
\|B'\|_\infty\le20/9,\quad
\|B''\|_\infty\le20.
$$
完整 $A$ 的 Fourier 导数 $\ell^1$ 范数实际为
$$
A_0<2.276867,\quad A_1<57.235136,\quad A_2<6809.7030.
$$
故 $\|\partial_r^d\partial_u^j Q\|\le\delta^{3-d}B_dA_j$。再用 [R230 的准确径向链](R230-m12-entire-original-source-jets-and-actual-field-transfer.md)及[完整旋转背景曲率证明](../notes/2026-11-09-db6f-audit-entire-background-curvature.md)：$E=1+w^2$、$|r_s|=E^{-1/2}\le1$，且 $|r_{ss}|=|ww_r|/E^2=(|w|/\sqrt E)|\kappa_r|\le6$。因此可取保守向外数值：

| 真实物理 jets | 严格上界 |
| --- | ---: |
| $|Q|$ | $2.900\times10^{-22}$ |
| $|Q_s|$ | $2.317\times10^{-14}$ |
| $|Q_u|$ | $7.288\times10^{-21}$ |
| $|Q_{ss}|$ | $3.0810\times10^{-6}$ |
| $|Q_{su}|$ | $5.823\times10^{-13}$ |
| $|Q_{uu}|$ | $8.671\times10^{-19}$ |

支撑上 $f=r\ge r_0$，因此相对**原未加 W 的准确基线**，完整 Gram 三角转移给
$$
\|(X+Q)^*e-g\|_g<2.572125\times10^{-8}.
$$
这只说明单节点消跳有极小的一阶预算，**没有求得等距修正，没有消掉其他原节点，也没有将 Q 偷加到已结束的 CI 场上**。新的供应器若要采用 (7)，必须明确新参考身份并实际重新消费全部残差；此处给出了准确公式、完整模式及预算。

## 6. 源、真实执行与复现

新源 `scripts/6a65-m12-exact-third-jet-jump.py`：SHA256
`63506a11d80e1d14e7e4b7dc7a5419b90fc198948772f76f2a6d9aa7ccd88e51`。

本次从原公开 blob 实际恢复并核验 Git framing hash 与 SHA256；完整有理 witness/补丁消费者实际 exit $0$，纯消费时间 $0.091$ 秒。标量报告保留 $r_0$、两侧长度、$A_x,A_z$ 的完整准确有理数，以及全部 $141$ 个 jump 通道的行流 hash，不发布原大数组。

```bash
python scripts/6a65-m12-exact-third-jet-jump.py \
  --scripts scripts \
  --source-transport raw-known-commit \
  --out "$FRESH_TEMP_DIR/m12-third-jump.json"
```

有已核恢复原件时可用 `--blob-file` 指定临时原块，程序仍核完整 hash。结论依赖上述明确的固定源/准确背景假设；任一新 g 或新源都不能沿用此具体 witness。

本次准确标量及补丁预算回执见 [真实有理消费者](../notes/2026-11-26-6a65-original-third-jet-jump-and-local-patch.json)。
