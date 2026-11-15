# R800：原146条 M2 新增尾 q129–195 的准确完成

日期：2026-11-15。状态：**公开 Actions 准确计算已完成；本篇只登记原截面的新系数，原函数关系、极除子、β、η和高度仍未完成。**

依据 [原方法](../notes/R800-original-M2-tail-129-195-method.md)、[R772 原下降](R772-original-RR-descent-and-exact-function-recovery-certificates.md)、[R781 原切向](R781-original-tangent-descent-and-inverse-free-Laurent-relations.md) 与 [R793 原RR接口](R793-original-RR-pole-divisors-and-CM-local-algebra.md)。

## 1. 实际结果

[公开 run43696070150](https://github.com/Rogerhu12/math-research-public/actions/runs/43696070150)，source **b53ef624e98b6cdbc9e59ad1bd7d33509dfdfc8c**，实际成功。核心证书记用时 **19.199004729000002秒**；外层回执于2026-11-15 08:47:07.933111 UTC完成，退出码0。

| 原对象 | 实际输出 |
|---|---|
| 原M2 | 146条，原索引与配方不变 |
| 唯一新范围 | $q_Y^{129},\ldots,q_Y^{195}$，每行67项 |
| 整数尺度 | $82^2=6724$ |
| 坐标 | 每项完整40个$\xi_{41}$坐标和20个原实切向$t$坐标 |
| 原E1新增尾 | 实际82条 |
| 原种子 | 原索引0、1、2、3、11，共200个种子coset尾 |
| 新系数有限域比较 | 全部通过原mod739对照 |
| 原实切向相位与反演 | 全部准确通过 |
| 已成输入 | 旧E1、M2、种子的0–128全部读取，没有重算 |

这些是保存输出中的实际数值，未由预期维数填入。实坐标来自原相位运输及逐项反演检验，不是以平均替代原展开。

## 2. 同一原截面的准确新系数

核心读取已认证R771/R775/R786的原配方、群与determinant相位、旧准确前缀。新E1除数和只处理$129\le mn\le195$；每个二积在相乘前排除不属于目标新区间的指标对。随后按原126群迹、40个determinant coset与6724尺度形成146条原M2尾。

所以新行由原公式的准确整数运算得到。mod739是有限域对照；准确配方、原相位和完整坐标负责其与原全球截面的识别。旧前缀的字节与SHA没有改写。

## 3. 源码与参数

| 项目 | 路径 | SHA-256 |
|---|---|---|
| 核心 | scripts/R800_original_M2_tail.py | 417dd598711af310717aaa971898e426d829a5209150bd5ce57f51dffb2e2a6a |
| 方法 | notes/R800-original-M2-tail-129-195-method.md | 5d1d299e5cbd293aaeb2929bd6ef694e6046296aad49956fae7f16de62b551ee |
| 公开wrapper | scripts/R800_public_original_M2_tail.py | 2783ff56f98bf9acdef4102eb0e7a6a0493224284d514705f1646e5fe53248a5 |
| 实际请求 | notes/R800-public-original-M2-tail-request.json | 709c0944070db0af4c7a6b0d83d6a0be6ebf52bfdb275f5bb9e2e6b1f67bbc15 |
| workflow | .github/workflows/serre-p41-original-M2-tail.yml | d84887afbeac0a1c692c2dd74ac1da5609babb2df43197fee60026b8496a2aa8 |

参数为first_exponent=129、last_exponent_exclusive=196；300分钟只作单次预算。原输入run为R771/43628998192、R775/43679160495、R786/43682100611；请求保存其准确来源和逐项输入SHA，不允许换基或模型。

## 4. 完成证据

| 输出 | 字节数 | SHA-256 |
|---|---:|---|
| p41-original-M2-tail-129-195-certificate.json | 37139 | 3be34598ab86732a790e7e5aa463b9def210fb48e216b9a51171d122e20ce377 |
| R800-stage-manifest.json.gz | 37969 | 17c93ee59632ae0bda21beeac90a24d0bdbfe74bb34c333705475aac9c17322b |
| R800-original-M2-tail-index.json.gz | 23767 | 13e6a2fa321ef67a16a7648fdf38f6ba95554677ba0b9fe6b76d5268db200da3 |
| full-outputs-manifest.json | 77560 | 1a651f6e0a3d51c8cb18d3b5fad18fb4d480f69e7bedd6e9fb10c7f80dbaf053 |
| R800-retained-producer-inputs.tar.gz | 5519019 | ce80fc35eb51b0a8a7cff2574e5aea57e60a6ccdb48fd6cd49c4deb770640831 |

完整清单共**439个输出文件**；阶段清单共**429个已成阶段**，包括82条新E1尾、200种子coset尾、146条M2尾及原顺序索引。

原artifact **14153948656**，名serre-global-R800-original-M2-tail-129-195-43696070150-1，ZIP **16486501字节**，SHA-256 **78ab2d6222f95015246dbfd4237c4ae2be8126971983bf6ee7173da8b1c83a4e**；保留至2026-11-16 08:47:08 UTC。

根环境失联期间，[公开纯IO run43699442183](https://github.com/Rogerhu12/math-research-public/actions/runs/43699442183)（source d9c4795a140a6815253f079eaf7936ac096a92ad）读取原ZIP，核实ZIP SHA、全部439项字节数/SHA、原source/request/core/wrapper，并调用原wrapper的verify(out)。09:29:01 UTC成功退出0，未调用数学核心。IO摘要SHA为7aa7785701bd6cb2d673b5da2ae06c2ed2cb6085a9b1b41dfed3f30953fc8fdd，保在一日artifact14156101148。

同次IO任务于09:28:56 UTC实际部分克隆及git pull --rebase origin main，读到0a7a0c88e20b3f7b69bf4dedf6cf347e4c6cdf81；相对4811fdaa的两份README差异为空。这是实际git回执。

## 5. 后继与边界

R801只消费原recipe闭包需要的M2新尾，并与原R786的0–128接合。本次没有生成power2–8、Laurent、原有理函数、极除子或高度。

可重算系数、完整证书与源输入包仅通过当前一日artifact/bundle续接。Git和Release不保存raw；本文保存脚本、参数、真实run/source与输出SHA。
