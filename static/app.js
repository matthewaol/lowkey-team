document.getElementById('meal-plan-form').addEventListener('submit', async (event) => {
        event.preventDefault(); // Prevent the default form submission
    
        const dishInputs = document.querySelectorAll('input[name="dish[]"]');
        const servingInputs = document.querySelectorAll('input[name="servings[]"]');
    
        const dishes = Array.from(dishInputs).map(input => input.value);
        const servings = Array.from(servingInputs).map(input => parseInt(input.value, 10));
    
        // Prepare data to send to the server
        const data = dishes.map((dish, index) => ({
            dish_name: dish,
            serving_number: servings[index]
        }));
    
        try {
            const response = await fetch('/generate-recipe', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data),
            });
    
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
    
            const result = await response.json();
            displayShoppingList(result); // Function to display the shopping list
        } catch (error) {
            console.error('Error:', error);
            alert('Failed to generate shopping list.');
        }
    });
    
    function displayShoppingList(data) {
        const shoppingListDiv = document.getElementById('shopping-list');
        shoppingListDiv.innerHTML = ''; // Clear previous results
    
        data.forEach(item => {
            const div = document.createElement('div');
            div.textContent = `Dish: ${item.dish_name}, Recipe: ${item.recipe}`;
            shoppingListDiv.appendChild(div);
        });
    }
    





// document.getElementById('meal-plan-form').addEventListener('submit', async function(event) {
//     event.preventDefault();  // 防止表单自动刷新页面
    
//     // 获取用户输入的数据. Gets the data entered by the user
//     const dishes = [...document.querySelectorAll('input[name="dish[]"]')].map(input => input.value);
//     const servings = [...document.querySelectorAll('input[name="servings[]"]')].map(input => input.value);

//     // 创建一个展示餐食的 div. Create a div that shows the meal
//     const displayMealsDiv = document.createElement('div');
//     displayMealsDiv.innerHTML = '<h2>Your Weekly Meal Plan:</h2>';
    
//     const mealList = document.createElement('ul');
    
//     // 遍历每一项 dish 和 servings，将其添加到展示区域. Go through each dish and servings and add them to the display area
//     dishes.forEach((dish, index) => {
//         const mealItem = document.createElement('li');
//         mealItem.textContent = `${dish} - ${servings[index]} servings`;
//         mealList.appendChild(mealItem);
//     });
    
//     displayMealsDiv.appendChild(mealList);
    
//     // 将生成的餐食列表插入到页面的表单下方. Insert the generated meal list below the form on the page
//     document.body.appendChild(displayMealsDiv);

//     // 这里你可以添加你的生成式 AI 接口调用，来获取食材清单
//     // 模拟请求 AI 接口并展示结果
//     // add Gemini generative AI interface call to get the ingredients list and display results
//     const response = await fetch('/api/generate-receipt', {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json',
//         },
//         body: JSON.stringify({ dishes, servings })
//     });

//     const shoppingList = await response.json();

//     // 显示生成的购物清单. Display the shopping list
//     const shoppingListDiv = document.getElementById('shopping-list');
//     shoppingListDiv.innerHTML = '<h2>Your Shopping List:</h2><ul>' +
//         shoppingList.map(item => `<li>${item}</li>`).join('') + '</ul>';
// });