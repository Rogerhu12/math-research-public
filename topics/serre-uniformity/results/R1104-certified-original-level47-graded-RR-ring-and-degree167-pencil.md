# R1104：原 full47 的完整五级 RR 乘法环与 degree167 pencil

日期：2026-11-27（Asia/Taipei）。会话：Astra-serre-24b8836b-20261126。
状态：**已证明；新公开精确计算成功。**

在原 $X=X_{\rm ns}^+(47)$、$q=4513$ 上，令
$\mathcal L=\Omega_X^1(C_\infty)$，沿 R1090 的原95元整来源及
全部23个cusps。本篇认证了 $\mathcal L^2$ 至 $\mathcal L^5$
的实际整乘法基、全部 cusp-vanishing 微分空间，
并由同一产品秩证明原第一、第二个section没有公共零点。
因此得到一个定义于原有限域上的、可分的 degree167 映射
$X_{\mathbf F_q}\to\mathbf P^1$。

本篇不给尚未计算的第三类微分、CM坐标或QC排点任何数值结论。

## 1. 实际公开回执

- source：
  [feaff1c23f0ddf90c6879cfaaf59811cdd17823e](https://github.com/Rogerhu12/math-research-public/commit/feaff1c23f0ddf90c6879cfaaf59811cdd17823e)；
- [run45964526314](https://github.com/Rogerhu12/math-research-public/actions/runs/45964526314)，
  [job140389923921](https://github.com/Rogerhu12/math-research-public/actions/runs/45964526314/job/140389923921)，attempt1；
- job和全部步骤success；数学耗时 **33.299813705秒**；
- 固定官方SageMath10.6 image digest，数学900秒、reserve30；
- root全文核原来源、算法和全部回执，并以canonical JSON重算completed对象SHA，
  与真实receipt一致。没有数学本地执行或新点扫描。

原R1090 Hodge证书仅按95个descriptor重建，核全部旧hash，
不重新选择来源或登记旧rank。新读取为同一来源到836项的展开、
四级实际产品及全部23个cusp上的消失条件。

## 2. 为什么836项足够，为什么这些秩证明整基

原 $g=73$、$\deg C_\infty=23$，所以
$\deg\mathcal L=167$。
标准尖点的实际参数是 $t=q_{\rm Tate}^{1/47}$；
R1090的section写为
$$
s_i=F_i(t)\,(47\,dt/t).
$$
$47\,dt/t$ 是原 $\mathcal L$ 的整单位标架。
产品的局部表示就是普通 $F_iF_j$，没有修改weight、微分或相位。

若 $s\in H^0(\mathcal L^n)$ 在此处的836项都为零，
其零除子在一个原点上的阶至少836。
对 $1\le n\le5$，非零section的总零次数却是
$167n\le835$，矛盾。因此原836-jet在这些空间单射。

又 $167n>2g-2=144$，Riemann–Roch给
$$
h^0(\mathcal L^n)=167n-72.
\tag{1104.1}
$$
消费者每一级保留的是实际前一级section与一个原95元section的产品，
没有把另一个曲线的积分基引入。
新模$q$秩达到(1104.1)，便证明产品张成整个原空间。

这些section有原整lift，$H^1(\mathcal L^n)=0$给整base change。
其模$q$独立minor是单位，Nakayama再给相应
$\mathbf Z_q$整section空间的基。
不把任意整数代表当作原section的lift。

## 3. 全部实际维数和产品范围

程序按source索引在外、前一级基索引在内的固定顺序考察产品，
批次大小95，达到目标即停；degree2删去对称重复。
最后source索引从0起计。

| n | 原 H0(L^n)维数 | 全23 cusp消失核维数 | 实际产品数 | 最后source索引 |
|---:|---:|---:|---:|---:|
| 2 | 262 | 239 | 282 | 2 |
| 3 | 429 | 406 | 524 | 1 |
| 4 | 596 | 573 | 858 | 1 |
| 5 | 763 | 740 | 1192 | 1 |

特别，$n=3,4,5$ 时只使用原前两个section作为右乘因子。
这不是预设的正常生成性质，而是实际完整产品跨度的回执。

R1090 的原23个留数除以47，给95个section的真实cusp值。
全部高次section的cusp值按同一产品索引递推。
对 $n\ge2$，
$$
\mathcal L^n(-C_\infty)=\Omega_X^1\mathcal L^{n-1},
$$
且次数大于144，故23条件应独立。
实际每个矩阵的核已核准，并得到上述239、406、573、740。
所以特别有真实来源
$$
U=H^0(\Omega_X^1\mathcal L^2),\quad \dim U=406,
\qquad
W=H^0(\Omega_X^1\mathcal L^4),\quad \dim W=740.
\tag{1104.2}
$$
未以单个cusp常数为零代替完整23条件；
$n=1$的总留数关系不被错搬到所有高次section。

## 4. 原前两section确实组成无基点pencil

记原95元基的前两section为 $s_0,s_1$。
新degree3回执中的524项准确是
$$
s_0H^0(\mathcal L^2)+s_1H^0(\mathcal L^2),
$$
其维数429，等于整个 $H^0(\mathcal L^3)$。

若 $s_0,s_1$ 的公共零除子是 $D$，
消去公共基点后的pencil exact sequence给
$$
0\longrightarrow\mathcal L(D)
 \longrightarrow(\mathcal L^2)^{\oplus2}
 \longrightarrow\mathcal L^3(-D)
 \longrightarrow0.
\tag{1104.3}
$$
$\deg D\le167$；两端的次数均大于144，所以 $H^1=0$。
于是上述实际乘法像的维数为
$h^0(\mathcal L^3(-D))=429-\deg D$。
实际值429迫 $\deg D=0$。

因此
$$
\boxed{\quad [s_0:s_1]:X_{\mathbf F_q}\longrightarrow\mathbf P^1
\text{ 是 degree167 的有限可分映射。}\quad}
\tag{1104.4}
$$
其pullback $\mathcal O(1)$ 是 $\mathcal L$，故degree167。
不可分次数是$q$的幂，而 $167<q$，所以它可分。
这是原曲线的真实有理函数 $s_1/s_0$，不只是抽象gonality上界。

进一步，有限flat pushforward $\pi_*\mathcal O_X$ 是rank167向量丛。
$\mathbf P^1$的向量丛分裂、$h^0(\mathcal O_X)=1$、
$h^0(\mathcal L)=95$ 和 $H^1(\mathcal L)=0$ 给
$$
\boxed{\quad
\pi_*\mathcal O_X
 \simeq \mathcal O
 \oplus\mathcal O(-1)^{93}
 \oplus\mathcal O(-2)^{73}.
\quad}
\tag{1104.5}
$$
这里所用的P¹分裂也可直接作归纳：取最大整数a使H⁰(E(−a))≠0，所得O(a)子丛因最大性已饱和。商丛按rank归纳分裂；若其中某O(b)有b>a，扭以−a−1后由H¹(O(−1))=0会提升出E(−a−1)的非零截面，矛盾。故b≤a，而全部Ext¹(O(b),O(a))=H¹(O(a−b))=0，扩张分裂。该论证在当前有限域上有效。

于是恰有一个degree0 summand，无正degree summand；
$H^1(\pi_*\mathcal O_X(1))=0$排除degree小于−2。
余下的−1 summand数是$95-2=93$，rank再给73个−2 summand。
这为后继有限函数域坐标提供了实际的原pencil，
但本篇尚未计算它的完整乘法表或Cartier矩阵。

## 5. 与原第三类微分的有限接口

若原Galois稳定reduced support $S$ 的degree不超过159，
则 $\deg\mathcal L^2(-S)\ge175>2g$，故全局生成。
对 $h,w\in H^0(\mathcal L^2(-S))$，
若公共零除子恰为$S$，逐点比较极阶给
$$
\{F\in U:Fw\in hU\}=hH^0(\Omega_X^1(S)).
\tag{1104.6}
$$
全部乘法只进入$W$，已在(1104.2)认证。
若额外公共零是$D$，同样的pencil exact sequence给
$$
\dim(hH^0(\mathcal L^3)+wH^0(\mathcal L^3))
 =763-\deg S-\deg D.
\tag{1104.7}
$$
所以实际维数$763-\deg S$也足以认证没有额外公共零。

这些式子给后继colon/Miller消费者一个明确有限来源。
实际$S$、粗参数、全部留数、$h,w$以及Cartier差仍须读取；
本篇不把源空间的张成等同于R1103所需$\alpha$已经求出。

## 6. 可复现来源与全部摘要

| 对象 | SHA-256 |
|---|---|
| 本次consumer | e54339e527a36ba15c4f2c799226a61ca8dcfc413fd0f9513819f44ac426ffa8 |
| 本次method | 66f7ce055a50c55de24d1b9de4aa03b324f8ec8616bf57672b0edbfafbf8345c |
| 本次request | 82fba83b0e46d98d16b0251baf3d04130ed41c683e65379fc019d42363ae94df |
| 原Hodge证书 | 4656ed9535d1df10776de395641342580b58f8d27727e64f2dfcb9b8db39498d |
| L^1 原836矩阵 | 4b1e6a1010a05009677087a734baa2d871d37eb92135cf9eea3d4e9a1b245706 |
| 完整completed对象 | 0d5077448b2c711306cce664ad9b6adbd5affb19bad5bd9388b8b561d636cc9c |
| L^2 原836基矩阵 | a854221bbfcbc1d43208ccfacadb7e2b65c89ab9d93a9c8dd035a2dc84046299 |
| L^2 产品索引 | 3f96bfc33d3a5b20800c7cb6b066fb01c0fbf951a3a14e5431161843583d61bb |
| L^2 全23 cusp评价 | 8f3065d82d98bce76aa0dbd24827c71334b588afd059b1df50acd68e5b8c388a |
| L^2 cusp核 | 7f6ce844cdaf7c0a5f8437e6dfa73eef830a646dad815cecde9c33bdf141562d |
| L^3 原836基矩阵 | 333a919cd240261bd45686f330ebcd36f0ef49cefec4ca4b3beee3adedb1685a |
| L^3 产品索引 | 040853df555de647306965a6464cf7372f6ae4ab743ab40a2c8aabfd0c426c8e |
| L^3 全23 cusp评价 | f218a4a3fbf049552200ce7a526ea694133d18fab668185a86bb2e21311fd74e |
| L^3 cusp核 | 98876a95c5173c862b42d25463d7481a01518bbee6462b96403155a598dfbb52 |
| L^4 原836基矩阵 | 72c27e1e3f9d4437e441f70198ae080cc682b61a3a18daae0d0d18641b4c6427 |
| L^4 产品索引 | b6ba509088befaea26577d70e05ee4a991b9761293dc3e429c28a5a450040779 |
| L^4 全23 cusp评价 | e1d7b76f69dd4cea9eb9a23de1bd0f63d5c2afd6296f7ca45db2f339a635bc42 |
| L^4 cusp核 | 2ee8ef3fa35762542823db2d893c2104d1e5ebaf8c2a089913ae3d6260858d38 |
| L^5 原836基矩阵 | 2368dd62b517f3cacc8cd2bb08adba7a6b4828777f1a994729682a83578b1a01 |
| L^5 产品索引 | 2b6f6f902b8cc21d7ab0721d4edd4d4ccd47a55b117df426f4d22e0c70f57aba |
| L^5 全23 cusp评价 | e50ba88423b59b1d355fc162fd171dc0d03198f60aac87448e617a216c52dd9c |
| L^5 cusp核 | f7ac41430708ccfed27290f9c415fb38f64247d7f69fc715e4f5365cd7e745a4 |

- [consumer](../scripts/full_p47_graded_RR_source.py)；
- [method](../notes/2026-11-27-full-p47-graded-RR-source-method.md)；
- [request](../notes/full-p47-graded-RR-source-request.json)；
- R1090原95元整来源、R1078原genus/cusps；RR、Serre对偶及pencil exact sequence的具体应用已在上文完整说明。

原矩阵、产品索引、级数只在runner scratch保留。
后继用同一确定性来源重建并核完整certificate，只消费已成输入；
不重开已证点筛、CM高矩或把输入重建登记为新结论。
Serre主目标和八盘最终唯一性继续OPEN。
