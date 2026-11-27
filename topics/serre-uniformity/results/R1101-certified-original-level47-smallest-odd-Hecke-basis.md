# R1101：原 full47 的实际最小奇 Hecke 整基

日期：2026-11-27（Asia/Taipei）。会话：Astra-serre-24b8836b-20261126。  
**状态：已证明，含精确有限计算。**

## 1. 结论

令 $q=4513$，$\mathcal T$ 为原 $X_{\rm ns}^{+}(47)$ 的
完整4513整 Hecke 代数。
[R1096](R1096-certified-original-CM-moving-units-and-odd-Hecke-height-basis.md)
已付 $H=T_3+T_5$、$\mathcal T=\mathbf Z_q[H]$、rank73。
本次准确取
$$
\boxed{\quad
\mathcal I=\{1,3,5,\ldots,149\}\setminus\{47,141\}.
\quad}
\tag{1}
$$
这73个实际算子 $\{T_n:n\in\mathcal I\}$ 构成原 $\mathcal T$ 的
$\mathbf Z_{4513}$ 整基。

若 $C$ 的第$n$行是 $T_n$ 相对
$1,H,\ldots,H^{72}$ 的升幂坐标，按$n$递增排列，则
$$
\boxed{\quad \det C=3946\pmod{4513}.\quad}
\tag{2}
$$
所有候选行从第一个起都增秩；
无需越过149，更没有运行至2255。
最大指标149、指标之和5437，是所有合法73指标集合的最小可能值；
这也直接由(1)是前73个正奇、prime-to47指标可见。

对原 $P_0=B_{4513}u_4$，
$\{T_nP_0:n\in\mathcal I\}$ 因而是原 MW 格在4513处的整基。
此处不声称它在所有素数处都是全局 $\mathbf Z$-基。

## 2. 实际来源与原 Hodge 坐标没有脱节

本次直接消费 R1090 原95个 descriptor、全部23尖点留数与
73维 Hodge 核的五个hash，
以及 R1093 的实际 $M_2,M_3,M_5,H_2$。
旧95行搜索、CM级数、秩、MW和标签均未重跑。

新的精确计算先在原 level2209、star sign1 的 modular symbols
中取完整 new space，再在每个simple factor上真实计算Fricke。
得到原 positive 三个轨道维数16、24、33；negative总维数84。
各轨道使用 normalized newform $f_i$，
以 $h_i=a_3(f_i)+a_5(f_i)$ 作为规范整生成元。

对任意 $n$，先在原数域的有理坐标中精确解
$$
a_n(f_i)=p_{i,n}(h_i),
$$
再核最终坐标分母全是$q$单位并约化。
三个 $h_i$ 最小多项式的乘积模$q$
准确等于原 $H=M_3+M_5$ 的特征多项式，
具有已经认证的同一hash和判别式2650。
CRT给 $p_n\in\mathbf F_q[X]/P$，且实际原算子
$T_n=p_n(H)$。

新消费者完整核了
$$
p_1(H)=I,\quad p_2(H)=M_2,\quad
p_3(H)=M_3,\quad p_5(H)=M_5,\quad
p_3+p_5=X\bmod P.
\tag{3}
$$
所以这个基在原 Hodge 的实际 row-action 中标定，
没有只凭特征多项式相同来猜同构，也没有借整 Chen 同源。

精确换域、CRT和有限域消元的全部证明与接口见
[小奇基方法](../notes/2026-11-27-full-p47-small-odd-Hecke-basis-method.md)。
原 $n\le2255$ 存在性由 R1096§8 的 Sturm2256 先已证明；
此次计算得到更小的实际最优集合(1)。

## 3. 真实公开运行

消费者：
[full_p47_small_odd_Hecke_basis.py](../scripts/full_p47_small_odd_Hecke_basis.py)；
参数：
[固定小奇基请求](../notes/full-p47-small-odd-Hecke-basis-request.json)。

- source commit：`049e7541c6ebfedc18dd6f4319dfb2445c050aa7`；
- [run45958934145](https://github.com/Rogerhu12/math-research-public/actions/runs/45958934145)；
- [job140371881297](https://github.com/Rogerhu12/math-research-public/actions/runs/45958934145/job/140371881297)；
- status：success；
- 完整数学时间：**18.667389850999996 秒**；
- 固定有限前缀：256、512、1024、2256；实际仅用第一个；
- 原官方 SageMath10.6 digest：
  `60dfb09e8d1399e127a0d7b62b45eef1044574bae397df51bb6ba38df5498879`。

首前缀读取 $a_0,\ldots,a_{255}$；
按$n$递增实际只检查73个合法候选，到149即rank73停止。
各$q$-expansion的 $a_0=0,a_1=1$ 与全部已读47倍系数零均核实。
没有浮点嵌入或舍入。

## 4. 复算hash与原参数

| 对象 | SHA-256 |
|---|---|
| 新消费者 | `5d91fd093580464c2fcecdd1b2e9abe751c4400eaa92374ec5e88931d6374dad` |
| 新方法 | `6fe837a5f5ad7e0897ec153c738976ec7cd5e821abc11b593cfd7bbde42d338f` |
| 新请求 | `0a513255a671853cc552603d2c6f8aebc5f5112743d9bc3503fe93166fba44e2` |
| 完整成功certificate对象 | `8607db54eb3232a0db99692057534830de4c3c0f291c39385c984174d233485e` |
| 实际73×73坐标矩阵 | `cd14a0499394d31b1c639ce76d0f34b4945ff8b7baa80a98072f3079ea0a0372` |
| 73指标升序列表 | `4e5918123ed7c3b003f147fed3f517dd1cb42225648ec59d3ede45c911e059ae` |
| 原 $H$ 矩阵 | `e0105e4915c8685dcac366c72bdad0d0c7ff2e5b0b72768d06fd5573fc31cfbf` |
| 原 $H$ 特征多项式 | `990a3205813f9785f40b97a754092530d9797edaee616b2814f2382530d06b37` |
| 维数16轨道 $h_i$ 整最小多项式 | `c6d16c60f41e162484ad208b3660cce80fad6d9b1a01218cfe459c2b6a39c730` |
| 维数24轨道 $h_i$ 整最小多项式 | `57f1c1b6f455c38a5ec7b32b6f26db601f00103ae2e2ca37e8919412a00e1743` |
| 维数33轨道 $h_i$ 整最小多项式 | `4706dd5aad5778d55b21eda7596abd55d8397f77014e7822cc380fd6a332e15e` |

最小多项式hash使用升幂**字符串**系数列表，
有限域多项式与矩阵hash使用升幂**整数**列表；
均按消费者compact sorted-key JSON。
不把两种序列化互换。

完整矩阵、数域坐标和Fourier长数组不入库、不上传artifact/Release。
(1)是下一次有限请求的确定指标参数；
长对象由脚本重建并核hash。

root核实际checkout/request/certificate hash及成功job；
root/global/o2全文纸审真实系数场坐标、CRT、row方向与有限前缀。
未安排重复程序执行。

## 5. 后继直接消费及其边界

固定调用
$$
\texttt{build\_basis(request,indices=I,expected\_certificate=certificate)}
$$
只重建绝对精度150的必要原输入及指定73行，
不会重新遍历或搜索候选。
完整certificate须和本次相同，
因此后继得到的是同一个实际整基。

随后令 $g_n=\Gamma(T_n)$，则
$$
(\Gamma(H^j))_{j=0}^{72}=C^{-1}(g_n)_{n\in\mathcal I}.
\tag{4}
$$
再通过原完美迹配对恢复完整$\kappa$，
逐28个不可约块检查单位。
已成[R1100](R1100-certified-original-level47-first-global-CM-height.md)
$\Gamma(1)=818$直接消费，其余72个高度才是新任务。

本条只支付完整高度的有限基及实际坐标。
完整高度结果、原八个 CM 管内部的排点、
以及所有充分大$p$的 Serre 主目标均继续。
