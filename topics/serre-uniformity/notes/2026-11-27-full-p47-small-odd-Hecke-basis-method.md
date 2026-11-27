# 原 full47 小奇指标 Hecke 整基：有限公开计算方法

日期：2026-11-27（Asia/Taipei）。
会话：Astra-serre-24b8836b-20261126。

状态：纸面证明和未执行消费者；本文没有新的数值回执。
唯一新目标是在原 $\mathcal T_{4513}$ 中选出73个小奇指标 $T_n$，
给出它们相对于 $1,H,\ldots,H^{72}$ 的规范整坐标，
其中 $H=T_3+T_5$。不计算高度、CM级数、$L'$或有理点。

## 1. 原来源和有限范围

[R1096§8](../results/R1096-certified-original-CM-moving-units-and-odd-Hecke-height-basis.md)
已经纸面证明
$$
\mathcal T_{4513}
=\sum_{\substack{1\le n\le2255\\n\ {\rm odd},\ 47\nmid n}}
 \mathbf Z_{4513}T_n .
\tag{OB.1}
$$
它对原 normalized newforms 应用
$f-V_2T_2f+2V_4f$，在层 $4\cdot47^2$ 使用 Sturm 界2256；
$U_{47}=0$删除47倍项，原$H$的73个互异剩余特征及 Nakayama
给整张成。没有将 Chen 同源当作整 Hodge 格同构。

消费者固定 $p=47,q=4513,N=2209$，Fourier绝对精度前缀为
$$
256,\ 512,\ 1024,\ 2256.
\tag{OB.2}
$$
精度$L$包含下标$0,\ldots,L-1$。各前缀严格递增读取奇数$n$、
$47\nmid n$；行秩达到73立即停止。
同一个factor、同一个coefficient-field name与$h$在各前缀中保留；
扩展后逐项核旧Fourier前缀完全不变。

数学预算900秒、reserve30秒，只用一个公开 SageMath10.6 job，
镜像沿原已审核的官方digest。超时只保已完成前缀与来源检查，
未完成的73维基不声明成功。没有会话内或本地数学执行。

## 2. 消费原95行、全部23尖点与三个实际矩阵

脚本
[full_p47_small_odd_Hecke_basis.py](../scripts/full_p47_small_odd_Hecke_basis.py)
只读既有
[full-p47-CM-height-move-request.json](full-p47-CM-height-move-request.json)，
固定SHA-256为
`bc89913668d6b3d209719a720c7562a7914459441526b6a565fc69edbfc2b7e6`。

从该文件取原95个descriptor、五个Hodge hash、
$M_2,M_3,M_5,H_2$的hash；不另复制长参数，也不使用其中旧CM数值
推导新结论。调用同一个原模块的
`build_source(descriptors=..., expected_certificate=...)`，
再调用`hecke_bridge(source)`。
只重建并核已有输入，不重搜95行或旧奇Hecke生成元。

全部23个尖点的真实$47c_0$残数、73维核和原相位均由该源保留。
原矩阵采用**行作用**
$T_n(\omega_i)=\sum_j M_n[i,j]\omega_j$。

本次消费的$H=M_3+M_5$矩阵与特征多项式hash分别为：

- 矩阵：
  `e0105e4915c8685dcac366c72bdad0d0c7ff2e5b0b72768d06fd5573fc31cfbf`；
- 特征多项式升幂整数列表：
  `990a3205813f9785f40b97a754092530d9797edaee616b2814f2382530d06b37`。

canonical JSON沿用
`json.dumps(value, sort_keys=True, separators=(",", ":"))`，
矩阵用原`integral_rows`，不改变整数/字串或升降幂约定。

## 3. 一次缓存序列的原newform输入

准确的modular-symbol来源为：

```python
ambient = ModularSymbols(2209, 2, sign=1, base_ring=QQ)
new = ambient.cuspidal_subspace().new_subspace()
factors = list(new.decomposition())
```

核ambient/cuspidal/new维数为$189,165,157$，
在每个完整new factor上实际求Fricke $w_{2209}$。
star sign$=1$不替代Fricke正号。
原正号三个factor维数为$16,24,33$，负号总维数84。

每个正号factor $A_i$、维数$d_i$，使用固定名称：

```python
f_i = A_i.q_eigenform(precision, names="alpha_%d" % d_i)
K_i = f_i.base_ring()
h_i = K_i(f_i[3] + f_i[5])
```

已亲读Sage10.6官方源码：

- [modsym/space.py](https://raw.githubusercontent.com/sagemath/sage/10.6/src/sage/modular/modsym/space.py)
  的`q_eigenform`缓存此前级数，再调用`eigenvalue`增加系数；
- [hecke/module.py](https://raw.githubusercontent.com/sagemath/sage/10.6/src/sage/modular/hecke/module.py)
  的`eigenvalue`对素数只计算一个稀疏ambient Heilbronn image，
  合数使用互素乘法和权二Hecke递推，不为每个$n$构造完整73维矩阵。

固定随机种子0使内部系数场构造可重现；
最终证书不依赖这个任意生成元。不使用浮点嵌入或舍入。
核$a_0=0,a_1=1$，以及已读前缀内全部47倍系数为零。
开启`proof.all(True)`；不向不接收该关键字的
QQ kernel/decomposition API额外传`proof=True`。

## 4. 先精确换到$h_i$，再模$q$

在$K_i$当前幂基中构造
$$
C_i[j,k]=[h_i^j]_k,\qquad 0\le j,k<d_i.
$$
各行是$1,h_i,\ldots,h_i^{d_i-1}$的坐标。
对$a_n(f_i)$，准确的行坐标为
$$
c_{i,n}=\operatorname{vec}(a_n(f_i))C_i^{-1},\qquad
p_{i,n}(X)=\sum_{j=0}^{d_i-1}c_{i,n,j}X^j.
\tag{OB.3}
$$
先在$\mathbf Q$和$K_i$中计算，核
$c_{i,n}C_i=\operatorname{vec}(a_n)$，
再逐个检查最终$c_{i,n,j}$分母为$q$单位。
不能先约化任意数域幂基或任意modular-symbol基。

令$P_i$为$h_i$首一最小多项式，准确转换到$\mathbf Z[X]$，
并核$\deg P_i=d_i$。
原$H$的73次特征多项式模$q$平方自由，故每个$h_i$生成完整系数场，
三个$P_i$模$q$两两互素，且各判别式为$q$单位。因此
$$
\mathbf Z_q[h_i]
=\text{该系数场在$q$处的最大有限étale整序}.
\tag{OB.4}
$$
$a_n$的整性给(OB.3)的分母单位性。

内部数域生成元即使改变，$h_i,a_n$也一起按同一个
$\mathbf Q$-嵌入变化；唯一关系$a_n=p_{i,n}(h_i)$保持不变。
因此$p_{i,n},P_i$是规范数据，不随内部字段表示改变。
后续缓存扩展必须保持同一个$h_i$和全部已读系数。

## 5. CRT和原Hodge的实际桥

在$k=\mathbf F_q$上令$P=\prod_i\overline P_i$，以及
$$
Q_i=P/\overline P_i,\qquad
E_i=Q_i(Q_i^{-1}\bmod\overline P_i)\pmod P.
$$
核$P=\chi_H$、$\deg P=73$、既有hash和平方自由，
各$\overline P_i$两两互素，$E_i^2=E_i$，$\sum E_i=1$。
定义
$$
p_n(X)=\sum_iE_i(X)\overline p_{i,n}(X)\pmod P,\qquad\deg p_n<73.
\tag{OB.5}
$$

原特征零Hecke对应把$T_n,H$送到$(a_n(f_i))_i,(h_i)_i$，
故已经证明原算子身份$T_n=p_n(H)$在$q$处成立。
(OB.4)和$\mathcal T=\mathbf Z_q[H]$保持其整性。
不是只根据“特征多项式相同”猜测对应关系。

新的有限接口仍须逐项核
$$
p_1(H)=I,\quad p_2(H)=M_2,\quad p_3(H)=M_3,\quad
p_5(H)=M_5,\qquad p_3+p_5=X\bmod P.
\tag{OB.6}
$$
原行作用直接代入多项式，不猜转置、period或另一个积分模型的基。
(OB.6)核实新系数与原Hodge来源的标签、规范及作用方向。

## 6. 有限贪心与输出

$p_n$始终用$([X^0]p_n,\ldots,[X^{72}]p_n)$表示。
按(OB.2)逐段，删偶数和47倍数，以准确有限域消元仅保增秩行，
满73行立即停止。由(OB.1)在界内完成。

所选行组成$C_{\rm small}$；其非零行列式给原$\mathbf Z_q$整基。
这也最小化候选集合中的$\sum n_i$：
线性拟阵基交换可把任一其它基依次改为贪心基而不增加权。

只输出73个真实指标、总和、最大值、行列式、坐标hash、
原$H,P$及三个规范$P_i$hash、实际桥检查和完成时间。
原始Fourier系数、数域坐标、73×73矩阵仅保留在runner中。
不创建artifact、Release或原始数组文件。

## 7. 后继固定指标调用

```python
built = build_basis(
    request,
    indices=old_certificate["indices"],
    expected_certificate=old_certificate,
    callback=progress,
)
```

`old_certificate`是成功回执的完整`certificate`对象，
不含外层时间、mode或`certificate_sha256`。
固定模式仅取绝对精度`max(6,max(indices)+1)`，
不遍历候选行或重做贪心。重建同一个$C_{\rm small}$后，
完整证书须相等，包含行列式、规范$P_i$及全部坐标hash。
调用者拥有总预算；API不改signal timer。

返回：

- `indices`；
- `coordinate_matrix`，原$C_{\rm small}$；
- `polynomial`，$P\in\mathbf F_q[X]$；
- `Hodd`，原行作用$H$；
- `hecke_polynomials`，$2,3,5$对应的$p_n$；
- `Hodge_operators`和`certificate`。

若后续真实得到$g_i=\Gamma(T_{n_i})$，则
$$
(\Gamma(H^j))_{j=0}^{72}=C_{\rm small}^{-1}(g_i)_{i=1}^{73}.
$$
再由$k[X]/P$完美迹配对恢复$\overline\kappa$，
才能检查全部28块单位性。
本请求不计算$g_i$，不重算已经认证的$\Gamma(1)$，
也不据一个非零迹值推断全部块非零。

## 8. request字段约定

根端负责发布request/workflow，需填：

```json
{
  "execution_id": "full-p47-small-odd-Hecke-basis-v1",
  "prime": 47,
  "coefficient_prime": 4513,
  "sage_version": "10.6",
  "total_seconds": 900,
  "reserve_seconds": 30,
  "precision_prefixes": [256, 512, 1024, 2256],
  "random_seed": 0,
  "height_move_request_path": "topics/serre-uniformity/notes/full-p47-CM-height-move-request.json",
  "height_move_request_sha256": "bc89913668d6b3d209719a720c7562a7914459441526b6a565fc69edbfc2b7e6",
  "Hodd_matrix_sha256": "e0105e4915c8685dcac366c72bdad0d0c7ff2e5b0b72768d06fd5573fc31cfbf",
  "Hodd_characteristic_polynomial_sha256": "990a3205813f9785f40b97a754092530d9797edaee616b2814f2382530d06b37",
  "source_sha256": {}
}
```

实际request的`source_sha256`必须填本脚本、本方法、
原Hodge模块和必要来源的真实hash，以环境变量
`SERRE_EXPECTED_REQUEST_SHA256`固定request自身。
消费者另外钉住旧request和原Hodge模块hash
`fe2e4f6b2420389b534fab0b2d1976dc6ac7cb2b1fe8ad98c07112ecd860afac`。
仅接受本公开仓库Actions及与`GITHUB_SHA`一致的checkout；
直接读取`.git`元数据，不依赖容器额外git程序。
