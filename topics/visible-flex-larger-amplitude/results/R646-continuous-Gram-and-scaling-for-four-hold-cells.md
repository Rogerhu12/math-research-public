# R646：同一 hold 前缀的六片连续 Gram 与比例二阶 jet 证书

**本条实际范围。** 对已经保存的同一 `aa1cf41f...` 完整 hold 开前缀，使用其原共同五次式、原固定 $q_{4096}$ 和同一精确积分度量，对胞 498、626、1905、2097 给出连续证书。626 与 1905 各被一个精确标量分界分成两片，共六片；每片分别执行完整 Gram 核和有限均值比例核，十二次均成功。六片最大的严格 Gram 算子上界为 **`2.1287021203818822e−7`**，小于 $10^{-6}$。

这不是新 IVP/BVP，不更改原候选；这里没有覆盖全部 2098 胞，也没有据此宣称曲率、reach、闭曲面或课题完成。原 pulse 的 819 片主批次没有改变。

## 1. 同一个精确标量初值

完整输入为仓库外 `parallel-negative-hold-complete-base.json.gz`，SHA256
`aa1cf41faf83a9e2b3e90167d0bc9e00e48c8d84cc2aec707c2da17c45f0ca15`。
它仍是已发表 hold 拼接定义的 M320、2099 个共同节点及保存的 0/1/2 jet；不是把旧 M112 左段二导用 M320 重新生成。

精确标量沿用 [R636](R636-certified-inward-reference-radius-and-length.md) 的旧 `.99` 三 jet 包围，先按同一个 $K=-a''/\sqrt{1-(a')^2}$ 运输到准确 binary `.995` cut。记得到的准确值为 $a_c,\alpha_c$；**没有把 `hold_scalar_profile.alpha0` 或 `kappa0` 的浮点记录作为另一个精确初值**。

令 $f,h,r$ 分别为 Python binary `.002,.02,.02` 对应的精确有理数，$k_n=-5/2,k_p=3/2$。定义

$$
S(u)=\begin{cases}0&u\le0,\\10u^3-15u^4+6u^5&0<u<1,\\1&u\ge1,\end{cases}
$$

$$
P(u)=\begin{cases}0&u\le0,\\\frac52u^4-3u^5+u^6&0<u<1,\\u-\frac12&u\ge1.\end{cases}
$$

以 $t=s-s_c$，在本候选所用的前三段内准确取

$$
\kappa(t)=K+(k_n-K)S(t/f)+(k_p-k_n)S((t-f-h)/r),
$$

$$
\alpha(t)=\alpha_c-Kt-(k_n-K)fP(t/f)
 -(k_p-k_n)rP((t-f-h)/r),
\qquad
a(s)=a_c+\int_0^t\sin\alpha(z)\,dz.
$$

这是已冻结 HoldProfile 的 fall/hold/rise 精确积分定义。代码中的普通浮点评价与各段 `start/shift` 只是其求值方式；本证书不把其舍入累积另定义成目标度量。

## 2. 积分和 Taylor 预算

从 $1.5<K<2.153$、$|\kappa|\le2.5$ 及
$\max S'=15/8$、$\max|S''|=10\sqrt3/3<6$，得到：

| 段 | $|\kappa'|$ 上界 | $|\kappa''|$ 上界 | 用于积分的 $|(\sin\alpha)''|$ 上界 | 用于三次 Taylor 的 $|a^{(4)}|$ 上界 |
|---|---:|---:|---:|---:|
| fall | 4362.1875 | 6979500 | 4370 | 7100000 |
| constant hold | 0 | 0 | 用准确原函数 | 16 |
| rise | 375 | 60000 | 382 | 63000 |

最后一列由准确恒等式

$$a^{(4)}=-\kappa''\cos\alpha-3\kappa\kappa'\sin\alpha+\kappa^3\cos\alpha$$

支付。各 ramp 积分分别使用固定 **4096 段中点法**；长度 $\ell$、对应第四列表值 $B$ 的积分误差为
$B\ell^3/(24\cdot4096^2)$。constant hold 段直接用

$$\int_u^v\sin\alpha(z)\,dz=
\frac{\cos\alpha(v)-\cos\alpha(u)}{k_n},$$

其中三角值与除法由同一个 R636 整数区间 oracle 包围。这样不把整段 `.025` 都按最陡的 fall 导数估计；同时没有更改精确积分对象。

报告中最大中点积分误差为 `1.1223959806597405e−13`。对每片的辅助三次式 $A$，0/1/2 阶 Taylor 误差仍分别为

$$M_4(\ell/2)^4/24,\qquad M_4(\ell/2)^3/6,\qquad M_4(\ell/2)^2/2.$$

它们都进入 Gram 或 $\lambda=a/\langle|F_\varphi|\rangle_{4096}$ 的完整二阶预算。498 的 $|\lambda''|$ 较宽，主要包括 `0.00021667480468649008` 的 $a''-A''$ 预算；未把辅助 $A''$ 冒作实际 $a''$。

## 3. 精确分界和固定计算范围

两个内部边界分别为

$$s_c+f=\frac{574731370046513215}{576460752303423488},\qquad
s_c+f+h=\frac{586260585092581685}{576460752303423488}.$$

前者落在原胞 626 的内部，其左节点为 `.9969999999999953`；后者落在原胞 1905 内部，其右节点为 `1.0170000000000694`。程序对原共同五次式做精确有理仿射限制，分别覆盖两侧闭子区间。很窄的一侧仍实际计算，既未挪动原场节点，也未删掉小片。

固定计划为 `498/all, 626/piece0, 626/piece1, 1905/piece0, 1905/piece1, 2097/all`。Gram 沿用 [R641](R641-continuous-Gram-certificate-for-one-pulse-cell.md) 的完整抵消式与连续 Bernstein/带权角覆盖，构造 N4096、证明角点 Q16384。比例三 jet 沿用 [R643 §7](R643-continuous-curvature-of-two-actual-pulse-cells.md) 的固定 N4096 有限均值核；它对径向仍连续覆盖。所有误差项、径向最高次数和物理角带宽都保留。

## 4. 实际结果

以下为程序的向外 binary 上界。对跨边界胞逐项取最大，得到完整原胞的 uniform 界；$1\pm d_0$ 构造比例区间时还须向外舍入。

| 原胞完整范围 | Gram 算子上界 | $|\lambda-1|$ | $|\lambda'|$ | $|\lambda''|$ |
|---|---:|---:|---:|---:|
| 498 | 2.1287021203818822e−7 | 5.662390347234583e−13 | 8.813270328624382e−10 | 0.00023280453950997283 |
| 626（两片并） | 1.1636264116813666e−7 | 6.938006861044175e−13 | 8.311855178038094e−12 | 9.430427546405024e−7 |
| 1905（两片并） | 1.2094672696899938e−7 | 7.664769598908979e−13 | 9.369723792637607e−12 | 1.4649542968491638e−6 |
| 2097 | 1.2961234534909596e−7 | 7.59670088740708e−13 | 1.8479023703115756e−11 | 4.335881054184678e−6 |

六片 Gram 依次为
`2.1287021203818822e−7, 1.1061330984563179e−7, 1.1636264116813666e−7, 1.208311347743575e−7, 1.2094672696899938e−7, 1.2961234534909596e−7`。
十二份报告均已读出，并验证完整预算为 finite、Gram/比例报告的精确端点一致、全部实际依赖 SHA 不变。

## 5. 冻结入口、报告身份与复现

入口 [hold连续证书源](../notes/2026-11-17-parallel-model-hold-continuous-certificates.py)，SHA256
`dc4b5579ba03dbe68220d82fb52a15f57b7b6cb273ae6d35326804629463ecc2`。
它仅生成已冻结 d066 Gram 或 e6ddb 节点核的 hold 标量／区间准备适配，不修改这两个旧源或当前 pulse 全域运行。生成核 SHA 分别为

- Gram：`8db915b8c5ac9f856d7faa7387265b857130e204bfcc402f37ff9f94c5597131`；
- finite nodes：`999fe3e215a2f9cbb19c086032d61ce8ef947df915f16ab65208b161824a71d1`。

以下文件都在仓库外，统一前缀为 `parallel-model-hold-`：

| 报告后缀 | SHA256 |
|---|---|
| `cell498-gram.json` | `0f2f7ca757c88d08fd67eaa12c859bdc173536bacc05568d8d72c0fd92f7a6be` |
| `cell498-nodes.json` | `09eb629131e891319c4e55caf76807d902fac890d2965e0d4e839d617d9ab743` |
| `cell626-piece0-gram.json` | `2f365008abe4645f179d7e74fa29529b6593f46d48af3b32112ac72cd9417f7a` |
| `cell626-piece0-nodes.json` | `74c82458631d372a8b5c774efbab25093a9227d3be0cc45276ff27a5cc730872` |
| `cell626-piece1-gram.json` | `c6c97dcfb101c70072295c10f770c848c66e1f931fb82266c7c7625cd40a7c74` |
| `cell626-piece1-nodes.json` | `13bcc3e3d828cc45bbce053f735a349c3d22b7d71fb3a89b1fdfd809571bdce3` |
| `cell1905-piece0-gram.json` | `6d98ccf624b7624fa0529d06230b44b18f62ff457231cc356b4dab98e5efcfae` |
| `cell1905-piece0-nodes.json` | `1df8b289fd7f2cfe43142853a4b7a6997f80f0aa9cd81599068e431876ace0e1` |
| `cell1905-piece1-gram.json` | `48e452f3179ad00f04997cdd05981be9dad33830fe0d63039bf3956f82a50a59` |
| `cell1905-piece1-nodes.json` | `61afbd7c80cbe11b974cd582f3b3ed34dc32285a45dffd62718e77e9e1a2bcc8` |
| `cell2097-gram.json` | `a96d3033da779ad5dc9cda70c655e1befe4a5669cf81b29afdef2ed7d1a2eee8` |
| `cell2097-nodes.json` | `afe5284f7c19fcf236959aec3843bd8a31f4cd7cf7e37ee79e408951e4a5612f` |

从仓库根执行，`WORK` 为仓库外工作目录。完整 aa1 输入沿已发表 hold C² 拼接源 `5f0390f9...` 再生，不需把 raw 入库。

```sh
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python \
  topics/visible-flex-larger-amplitude/notes/2026-11-17-parallel-model-hold-continuous-certificates.py \
  --input "$WORK/parallel-negative-hold-complete-base.json.gz" \
  --engine topics/visible-flex-larger-amplitude/notes/2026-11-17-parallel-model-pulse-gram-representative-cells.py \
  --node-kernel topics/visible-flex-larger-amplitude/notes/2026-11-17-parallel-model-arclength-lambda2-node-kernel.py \
  --hold-source topics/visible-flex-larger-amplitude/scripts/parallel_20261117_negative_hold_profile_ivp.py \
  --interval-source topics/visible-flex-larger-amplitude/scripts/parallel_20261117_arclength_interval_positive.py \
  --scalar-oracle topics/visible-flex-larger-amplitude/notes/2026-11-17-parallel-inward-integral-enclosure.py \
  --cell 498 --mode gram \
  --out "$WORK/parallel-model-hold-cell498-gram.json"
```

将 `--mode` 换成 `nodes` 取得同片比例三 jet；另外按固定计划替换 `--cell`，626/1905 必须分别带 `--piece 0` 与 `--piece 1`。Q16384/N4096 与 scalar4096 在入口固定。每个 Gram 约 10.6–15.6 秒，nodes 约 3.9–6.1 秒，均为本次实际观测。报告含时间与实际路径，因此重跑整文件 SHA 不保证相同；数学对象、完整预算及来源均由冻结入口明确绑定。
