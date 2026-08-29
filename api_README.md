# Optional ModelScope API Setup

1. Register for a [ModelScope](https://www.modelscope.cn/) account.
2. Read the [guide to using free ModelScope models](https://www.modelscope.cn/learn/1409).
3. Browse the [list of free ModelScope models](https://modelscope.cn/models?filter=inference_type&page=2&tabKey=task).
4. Open a specific model page, such as [Qwen/Qwen3.8-27B](https://modelscope.cn/models/Qwen/Qwen3.8-27B).

   ![ModelScope model details page](image.png)

5. Find the code example that uses the Anthropic API protocol.

   ![Anthropic-compatible API example on ModelScope](image-1.png)

6. Create a new API token. ModelScope will provide the API base URL and API key.
7. Start Claude Code with the model configuration:

   ```bash
   export ANTHROPIC_MODEL=Qwen/Qwen3.8-27B  # Model name selected above
   export ANTHROPIC_BASE_URL=https://api-inference.modelscope.cn  # API base URL
   export ANTHROPIC_AUTH_TOKEN=<YOUR_MODELSCOPE_API_TOKEN>  # API key
   claude
   ```

   Never commit a real API token to this repository or share it in screenshots, prompts, or logs.

8. Start learning and working with Claude Code.
9. For the fastest course path, use the planning prompt (`prompts/plan.txt`) and then the implementation prompt (`prompts/build-dashboard.txt`).
